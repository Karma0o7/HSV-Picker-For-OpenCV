import cv2
import numpy as np
import stackImgModule as sim

def empty(a):
    pass

def createWindow():
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

def main():
    stacker = sim.ImageStacker()
    createWindow()
    try:
        while True:
            img = cv2.imread(r"Hsvpicker\assets\lambo.png")
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
            h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
            s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
            s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
            v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
            v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
            lower = np.array([h_min, s_min, v_min])
            upper = np.array([h_max, s_max, v_max])
            mask = cv2.inRange(imgHSV, lower, upper)
            imgResult = cv2.bitwise_and(img, img, mask=mask)
            imgStack = stacker.stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
            cv2.imshow("Stacked Images", imgStack)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                cv2.destroyAllWindows()
    except cv2.error:
        print("Tracker Window Closed.")

if __name__ == "__main__":
    main()

