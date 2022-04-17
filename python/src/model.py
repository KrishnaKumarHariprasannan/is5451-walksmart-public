import os
import torch

from functools import cached_property

MODEL_CHECKPOINT_PATH = "../../data/checkpoints/mlp.pth"
CNN_MODEL_CHECKPOINT_PATH = "../../data/checkpoints/cnn.pth"


class _ClassificationNetMLP(torch.nn.Module):
    def __init__(self, input_size=225, hidden_size=50, output_size=2):
        super(_ClassificationNetMLP, self).__init__()
        self.pred_net = torch.nn.Sequential(
            torch.nn.Linear(input_size, hidden_size),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.5),
            torch.nn.Linear(hidden_size, output_size),
        )
        self.load_model()
        self.eval()

    @cached_property
    def device(self):
        return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def load_model(self):
        if os.path.exists(MODEL_CHECKPOINT_PATH):
            self.load_state_dict(
                torch.load(MODEL_CHECKPOINT_PATH,
                           map_location=str(self.device),)
            )
        else:
            print(f"Model state not found at {MODEL_CHECKPOINT_PATH}")

    def forward(self, x):
        scores = self.pred_net(x)
        return scores


class _ClassificationNetCNN(torch.nn.Module):
    def __init__(self):
        super(_ClassificationNetCNN, self).__init__()
        self.conv1 = torch.nn.Conv1d(1, 20, kernel_size=3, padding=1)
        self.conv2 = torch.nn.Conv1d(20, 10, kernel_size=3, padding=1)
        self.linear = torch.nn.Linear(1120, 2)

        self.load_model()
        self.eval()

    @cached_property
    def device(self):
        return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def load_model(self):
        if os.path.exists(CNN_MODEL_CHECKPOINT_PATH):
            self.load_state_dict(
                torch.load(CNN_MODEL_CHECKPOINT_PATH,
                           map_location=str(self.device),)
            )
        else:
            print(f"Model state not found at {CNN_MODEL_CHECKPOINT_PATH}")

    def forward(self, x):
        # 1 * 225 -> 20 * 225
        y = self.conv1(x)
        y = torch.relu(y)
        # 20 * 225 -> 20 * 112
        y = torch.max_pool1d(y, 2)

        # 20 * 112 -> 10 * 112
        y = self.conv2(y)
        y = torch.relu(y)

        y = y.view(-1, 1120)

        # n * 1120 -> n * 2
        scores = self.linear(y)
        return scores


# NOTE: Use MLP model for prediction in our cloud server as the performance is similar for both
# models and MLP has a fairly simple architecture
fall_detection_model = _ClassificationNetMLP()
