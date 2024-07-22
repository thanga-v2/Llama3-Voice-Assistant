import cv2

webcam = cv2.VideoCapture(0)

def webcam_capture():
    if not webcam.isOpened():
        print('Error: Not Successfully opened. Exit')
        exit()

    else:
        print("Good")

    path='webcam.jpg'
    ret, frame = webcam.read()
    cv2.imwrite(path, frame)


webcam_capture()

