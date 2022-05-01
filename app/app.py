from pathlib import Path
from typing import Optional, Union

import cv2
import face_recognition
import numpy as np


class Application:
    def __init__(self, model, ui) -> None:
        self.captured_images = Optional[np.ndarray]
        self.model = model
        self.ui = ui

    def capture_image(self, video_source: Union[int, str]) -> None:
        video = cv2.VideoCapture(video_source)
        while True:
            _, frame = video.read()
            frame_with_box = frame.copy()
            for top, right, bottom, left in face_recognition.face_locations(frame):
                cv2.rectangle(
                    frame_with_box, (left, top), (right, bottom), (0, 255, 0), 3
                )
            cv2.imshow("Capturing...", frame_with_box)
            if cv2.waitKey(1) == ord("q"):
                self.captured_images = frame
                cv2.destroyAllWindows()
                break

    def register_user(self, reference_images: str) -> None:
        answer = input("Are you an unregistered user? <y/n> ").lower()
        if answer == "y":
            user = input("Enter your name: ")
            image_path = str(Path(reference_images) / (user.replace(" ", "") + ".jpg"))
            cv2.imwrite(image_path, self.captured_images)
            print(f"Welcome, {user}!")
        elif answer == "n":
            print("Unable to recognize user.")
        else:
            print("Your answer must be 'y' or 'n'.")
            self.register_user(reference_images)

    def display_prediction(self, reference_images: str) -> None:
        self.model.fit(reference_images)
        user = self.model.predict(self.captured_images)
        if user is None:
            self.register_user(reference_images)
        else:
            print(f"Welcome, {user}!")
