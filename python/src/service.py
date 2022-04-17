import ast
import numpy as np
import pickle
import torch

from flask import Flask, request
from datetime import datetime

from model import fall_detection_model

app = Flask(__name__)
EXPECTED_DATA_LENGTH = 75
FILE_IDX = 0

# NOTE: Update path below to your local folder
TEMP_DATA_BASEPATH = r"C:\Users\Rishabh\OneDrive\Desktop\nus_study\is5451-walksmart\data\raw\service_inputs\{}_{}.pickle"


# Given that there are no other APIs hosted in the service, use the root "/"
# as the route to fall detection API.
# NOTE: In case the above changes, the path should be updated below
@app.route("/", methods=["POST"])
def detect_fall():
    json_data = request.json
    print("json_data: ", json_data)
    # result = process_and_predict(np.array(json_data['data']))
    result = process_and_predict(np.array(ast.literal_eval(json_data["data"])))
    return {"result": result}


def process_and_predict(input_arr):
    global FILE_IDX
    data_points = []
    for start_idx in np.arange(0, input_arr.shape[0], 70):
        data_points.append(
            input_arr[start_idx: start_idx + EXPECTED_DATA_LENGTH])

    last_point = data_points[len(data_points) - 1]

    if len(last_point) < EXPECTED_DATA_LENGTH:
        # Repeat values from last row till we reach EXPECTED_DATA_LENGTH
        last_row = last_point[last_point.shape[0] - 1]
        data_points[len(data_points) - 1] = np.vstack(
            [
                last_point,
                np.vstack(
                    [last_row] * (EXPECTED_DATA_LENGTH - last_point.shape[0])),
            ]
        )

    results = []
    flag = 0
    for data_point in data_points:
        model_out = (
            fall_detection_model(torch.Tensor(
                data_point.transpose(1, 0).flatten()))
            .argmax(0)
            .item()
        )
        results.append({"input": data_point.tolist(), "output": model_out})
        if model_out == 1:
            flag = 1

    # Save sensor readings on disk along with the result for improving the
    # ML model
    folder_name = datetime.now().strftime(format="%d_%m_%Y")
    with open(TEMP_DATA_BASEPATH.format(folder_name, FILE_IDX), "wb") as f:
        pickle.dump(results, f, pickle.HIGHEST_PROTOCOL)
        FILE_IDX += 1

    return flag
