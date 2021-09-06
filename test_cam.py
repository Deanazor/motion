from cv2 import VideoCapture, resize, INTER_CUBIC, imshow, waitKey, destroyAllWindows
from app import detect
cap = VideoCapture(0)
img_bg = None
# cv2.namedWindow("Input", cv2.WINDOW_NORMAL) 
# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Can't open webcam")

while True:
    ret, frame = cap.read()
    dim = (1280,720)
    frame = resize(frame, dim, interpolation=INTER_CUBIC)

    if img_bg is not None :
        frame = detect(img_bg, frame)
        frame = resize(frame, (1280, 720), interpolation=INTER_CUBIC)

    imshow('Input', frame)

    action = waitKey(1)
    if action == 27:
        # print(frame.shape)
        break
    elif action == ord('t'):
        img_bg = frame
        imshow("Taken", img_bg)

cap.release()
destroyAllWindows()