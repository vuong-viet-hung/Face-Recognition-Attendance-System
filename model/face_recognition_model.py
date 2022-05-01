from pathlib import Path
from typing import Dict, Optional

import cv2
import face_recognition
import numpy as np


def path_to_label(image_path: Path):
    return image_path.stem


def encode_face(image: np.ndarray):
    face_location = face_recognition.face_locations(image)
    return np.array(face_recognition.face_encodings(image, face_location)[0])


class FaceRecognitionModel:
    def __init__(self) -> None:
        self.classes: Optional[Dict[int, str]] = None
        self.known_face_encodings: Optional[np.ndarray] = None

    def fit(self, reference_images: str) -> None:
        reference_images = Path(reference_images)
        labels = [
            path_to_label(image_path) for image_path in reference_images.iterdir()
        ]
        self.classes = dict(zip(range(len(labels)), labels))
        self.known_face_encodings = np.array(
            [
                encode_face(cv2.imread(str(image_path)))
                for image_path in reference_images.iterdir()
            ]
        )

    def predict(self, image: np.ndarray) -> Optional[str]:
        # There aren't any registered users.
        if not len(self.known_face_encodings):
            return
        face_encodings = encode_face(image)
        # There aren't any known matched faces.
        if not np.any(
            face_recognition.compare_faces(self.known_face_encodings, face_encodings)
        ):
            return
        prediction = np.argmin(
            face_recognition.face_distance(self.known_face_encodings, face_encodings)
        )
        return self.classes[prediction]
