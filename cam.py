from cv2 import VideoCapture, resize, INTER_CUBIC, imshow, waitKey, destroyAllWindows
from motion.detection import m_detect
import argparse

height = 720
width = 1280
threshold = 0.75

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r",
    "--row",
    default=height,
    type=int,
    help="Input your desired window height",
)

parser.add_argument(
    "-c",
    "--col",
    default=width,
    type=int,
    help="Input your desired window width",
)

parser.add_argument(
    "-t",
    "--threshold",
    default=threshold,
    type=float,
    help="Input your desired threshold",
)

value_parser = parser.parse_args()

def main():
    global width, height, threshold
    cap = VideoCapture(0)
    width = value_parser.col if value_parser.col is not None else width
    height = value_parser.row if value_parser.col is not None else height
    dim = (width, height)
    threshold = value_parser.threshold if value_parser.threshold is not None else threshold
    img_bg = []
    play = False

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Can't open webcam")
            
    while True:
        _, frame = cap.read()
        frame = resize(frame, dim, interpolation=INTER_CUBIC)

        if play:
            frame = m_detect(img_bg, frame, threshold)
            frame = resize(frame, dim, interpolation=INTER_CUBIC)

        imshow('Input', frame)

        action = waitKey(1)
        if action == 27:
            break
        elif action == ord('t') and not play:
            img_bg.append(frame)
        elif action == ord('r') and not play:
            img_bg = []
        elif action == ord('p') and len(img_bg) > 0:
            play = True
        elif action == ord('s'):
            play = False

    cap.release()
    destroyAllWindows()

if __name__ == "__main__":
    main()