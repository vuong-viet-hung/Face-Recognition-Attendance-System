from fras import Application

WEBCAM = 0


def main() -> None:
    app = Application()
    app.capture_image(video_source=WEBCAM)
    app.display_prediction("data/reference_images")


if __name__ == "__main__":
    main()
