import cv2


def camera():
    cam = cv2.VideoCapture(0)
    return cam


def picture(filename):
    image = cv2.imread(filename)
    return image
