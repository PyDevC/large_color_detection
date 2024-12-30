import cv2
import numpy as np


def hsvframe(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernal = np.ones((5, 5), "uint8")


def red_color(hsvFrame, kernal):
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)

    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(frame, frame, mask=red_mask)

    contour(hsvFrame, red_mask, "red")


def green_color(hsvFrame, kernal):
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)

    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(frame, frame, mask=green_mask)

    contour(hsvFrame, green_mask, "green")


def blue_color(hsvFrame, kernal):
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)

    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    contour(hsvFrame, blue_mask, "blue")


def contour(frame, mask, color):
    contours, hierarchy = cv2.findcontours(mask,
                                           cv2.retr_tree,
                                           cv2.chain_approx_simple)

    for pic, contour in enumerate(contours):
        area = cv2.contourarea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingrect(contour)
            imageframe = cv2.rectangle(frame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.puttext(imageframe, f"{color} colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
