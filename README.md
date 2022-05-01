# Face Recognition Attendance System

## I. Description
**Face Recognition Attendance System (FRAS)** registers new members using their fingerprints and face images. Member can then enroll by capturing their picture through a webcam.

## II. Hardware requirements
1. AS608 fingerprint sensor
2. Arduino UNO R3
3. Raspberry PI
4. Webcam
5. Keypad (Optional)

## III. Project Flowchart
![Project Flowchart (without keypad)](Project_Flowchart-without_keypad.png "Project Flowchart (without keypad)")
### A. Project with keypad
#### a. Register or enroll using fingerprint 
1. Member's fingerprint is detected by the AS608 sensor.
2. The program **(sensor/)** uploaded to Arduino checks if the fingerprint matches a registered one and send the result to Raspberry PI via serial port.
3. The program **(serial_reader/)** executed on Raspberry PI read and log the info packets from Arduino to the console.
The member's student ID and time of enrollment is then saved to a csv file **(serial_reader/matches.csv)**. 
4. If the sensor is unable to match with an existing fingerprint, the program **(serial_reader/)** should prompt the member to place their finger again.
If not, the program should assign the fingerprint with an increasing ID.
5. The program **(serial_reader/)** prompts the member to enter his/her student ID.
6. Webcam connected to Raspberry capture the member's face image.
7. The member's fingerprint ID, student ID and the path to his/her face images is stored in the database.
#### b. Enroll using image
8. Webcam connected to Raspberry capture the member's face image.
9. The program **(fras/)** compares the member's newly captured image with existing ones stored in the database.
10. The respected member's student ID is looked up in the database.
11. The member's student ID and time of enrollment is then saved to a csv file **(serial_reader/matches.csv)**.

![Project Flowchart (with keypad)](Project_Flowchart-with_keypad.png "Project Flowchart (with keypad)")
### B. Project without keypad
#### a. Register
1. Member's fingerprint is detected by the AS608 sensor.
2. The program **(sensor/)** uploaded to Arduino assign member fingerprint with an increasing ID.
3. Webcam connected to Raspberry capture the member's face image.
4. The member's fingerprint ID, student ID and the path to his/her face images is stored in the database.
#### b. Enroll
5. Webcam connected to Raspberry capture the member's face image.
6. The program **(fras/)** compares the member's newly captured image with existing ones stored in the database.
7. The respected member's student ID is looked up in the database.
8. The member's student ID and time of enrollment is then saved to a csv file **(serial_reader/matches.csv)**.

## IV. Installation
The project uses [Poetry](https://python-poetry.org/) as packages and environment manager. In order to install Poetry, follow the [installation guide](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions). \
Run the flowing commands inside the project directory:

```
poetry install
```
to install project dependencies.
```
poetry shell
```
to activate the environment.
