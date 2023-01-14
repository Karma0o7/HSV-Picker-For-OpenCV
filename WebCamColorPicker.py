import cv2
import numpy as np

frameWidth = 140
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

def createWindow():
    cv2.namedWindow("HSV Picker")
    cv2.resizeWindow("HSV Picker", 640, 240)
    cv2.createTrackbar("HUE Min", "HSV Picker", 0, 179, empty)
    cv2.createTrackbar("SAT Min", "HSV Picker", 0, 255, empty)
    cv2.createTrackbar("VAL Min", "HSV Picker", 0, 255, empty)
    cv2.createTrackbar("HUE Max", "HSV Picker", 179, 179, empty)
    cv2.createTrackbar("SAT Max", "HSV Picker", 255, 255, empty)
    cv2.createTrackbar("VAL Max", "HSV Picker", 255, 255, empty)

def main():
    createWindow()
    try:
        while True:
            _, img = cap.read()
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h_min = cv2.getTrackbarPos("HUE Min", "HSV Picker")
            s_min = cv2.getTrackbarPos("SAT Min", "HSV Picker")
            v_min = cv2.getTrackbarPos("VAL Min", "HSV Picker")
            h_max = cv2.getTrackbarPos("HUE Max", "HSV Picker")
            s_max = cv2.getTrackbarPos("SAT Max", "HSV Picker")
            v_max = cv2.getTrackbarPos("VAL Max", "HSV Picker")

            lower = np.array([h_min, s_min, v_min])
            upper = np.array([h_max, s_max, v_max])
            mask = cv2.inRange(imgHSV, lower, upper)

            result = cv2.bitwise_and(img, img, mask=mask)
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

            hStack = np.hstack([img, mask, result])
            cv2.imshow('Horizontal Stacking', hStack)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except cv2.error:
        print("Tracker Window Closed")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()