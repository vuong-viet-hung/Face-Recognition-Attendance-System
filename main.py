from app import Application
from model import FaceRecognitionModel
from user_interface import CLI


WEBCAM = 0


def main() -> None:
    app = Application(model=FaceRecognitionModel(), ui=CLI())
    app.capture_image(video_source=WEBCAM)
    app.display_prediction("data/reference_images")


if __name__ == "__main__":
    main()
