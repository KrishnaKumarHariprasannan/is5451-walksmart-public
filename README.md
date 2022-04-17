# is5451-walksmart

Group Number: 1

## Contact Details

1. Name: Khor Hui Shan, Felicia (Group Leader)

   Matriculation Number: A0115301A

   E-mail: fkhor@u.nus.edu

2. Name: Krishna Kumar Hariprasannan

   Matriculation Number: A0229171H

   E-mail: krishnakh@u.nus.edu

3. Name: Ng Hui Ling

   Matriculation Number: A0230406W

   E-mail: e0695926@u.nus.edu

4. Name: Rishabh Sheoran

   Matriculation Number: A0236146H

   E-mail: rishabh.sheoran@u.nus.edu

## YouTube

https://www.youtube.com/watch?v=6y2OkuKH1Pg&ab_channel=SweetDream

## Setup

### (A) Microbit

Flash the code provided in the file -> "microbit/microbit_bluetooth_activity.js"
on a Micro:bit (v1)

This is required to start the accelerometer bluetooth service and add required event handlers for tracking steps. Once the code is flashed, wear the microbit as shown in the demo video on your footwear.

### (B) Cloud Server

The cloud server hosts the service required to detect falls (using ML model). The server is a flask application with only one end-point that serves the API for fall detection. To bring up the cloud server, follow the below instructions.

MAC/Linux::
cd python/src/
export FLASK_APP=service.py
flask run --host=0.0.0.0 --port 5001

Windows::
cd python/src/
set FLASK_APP=service.py
flask run --host=0.0.0.0 --port 5001

Please note the below to complete the cloud server setup

1. Connect the mobile and server to the same WiFi (in case you are using localhost server).
2. In 'android\walksmart\app\src\main\java\com\example\myapp\activity\MainActivity.java', change the FALL_SERVER_URL path to the URL where the server is hosted (you can see this path when you start the server).

### (C) Android

- Run WalkSmart app on the phone using android studio (or using the APK provided). Pair your phone to the Micro:bit via bluetooth.

- Press the 'Details' button next to 'Fall Detection' text and add the name and contact number of the Emergency Contacts. You can view it in the list below the EditText fields. To remove an emergency contact, just tap on the entry in the list.

- Press 'Enable Walksmart' to get the permissions and the accelerometer and steps data from the Microbit. You will be able to see '##########accelerometerData size: ' being printed in the Logcat of android studio if the android is receiving data from the microbit.

### (D) Social Lighting

1. Flash the code provided in the file -> "microbit/social_lighting.js" on two Microbits (v1). Please load the NeoPixel driver and Radio functionality on the Microbit MakeCode Editor. Each Microbit needs to be connected with a Microbit Groove Shield and LED Strip.
2. The LED strip should display an Indigo color. Press Button A to start the Social Lighting through the radio functionality (to start detecting and sending strings through radio).
3. Upon detecting another Microbit (by receiving Radio strings), the LED strip changes to a Rainbow color.
4. If the other Microbit is out of range, the LED strip will change back to an Indigo color after 3 seconds.

### (E) Historical Activity Data

Simulated historical steps activity data is available in the form of a json file (under `android/walksmart/app/src/main/assets/dummy.json`) and is auto-populated the first time you visit the Activity Details screen. This is automatically done in the code and requires no explicit setup from the user.

## Working with the App

Once the above setup steps are done, you are now ready for the WalkSmart experience. The app starts receiving sensor readings from the Micro:bit and goes about processing and presenting the processed information through different activities in the app.

Once the android receives 500 entries from the accelerometer, it sends the data to the server. If the neural network model on the server detects a fall, it will send back the result as '1'. This creates an alert dialog box on the app. If the user does not take any action in 10 seconds or presses the 'Confirm' button, the app sends a message with the location of the user to the emergency contacts. The user can press the 'Cancel' button if it is a false alarm to cancel the sending of the message.

The user can see the number of steps taken by him/her by pressing the refresh button next to the Progress bar. The user can also set a daily target of steps. To set a target, the user should press the 'Details' button next to the progress bar. Fill in a target in the EditText box below 'Your Daily Target' text and press the save button. When the user presses the back button, he/she can see that the progress of number of steps taken for the day is shown in the progress bar relative to the target set by the user.

## Known Issues

- Android's BLE connection to Micro:bit has proved to be unstable on more than one occasion. In case your connection is unstable, unpair the device, restart app and connect again. Once, the app starts receiving the data, the app is ready to use.

Please reach out to one of the team members listed above in case of any issues with the setup.
