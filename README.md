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
<center>Project Flowchart (without keypad)</center>

<br/>

![Project Flowchart (with keypad)](Project_Flowchart-with_keypad.png "Project Flowchart (with keypad)")
<center>Project Flowchart (with keypad)</center>

## IV. Installation
The project uses [Poetry](https://python-poetry.org/) as packages and environment manager. In order to install Poetry, follow the [installation guide](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions). \
Run the flowing command inside the project directory.

```
poetry init
```
to activate the enviroment.
```
poetry install
```
to install project dependencies.