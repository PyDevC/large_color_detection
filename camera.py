import cv2

# camera features will be updated making it compatible for other devices


def camera():
    cam = cv2.VideoCapture(0)
    return cam


def picture(filename):
    image = cv2.imread(filename)
    return image
