import cv2
import numpy as np
import addon_function as my

cap = cv2.VideoCapture(0)

# FOR POSITION AND SIZE OF CALC
values = np.loadtxt('data/values.txt', int)
x = values[0]
y = values[1]
h = values[2]
w = values[3]

# VARIABLES
ans = ""
ab = ""
a, b = -1, -1
approx = 0
prev_approx = 0

while cap.isOpened():

    # READ AND RESIZE FRAME
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (800, 600))

    # REGION OF INTEREST
    roi = frame[:, 400:]

    # CONVERT FRAME TO B/W
    thres = my.thresold(roi)

    if len(ab):
        a = int(ab[0])
        b = int(ab[1])
        s = int(ab[2])
        clr = (0, 190, 0)
        if s == 0:
            cv2.rectangle(frame, (x + w * a, y + h * (2 + b)), (x + w * (a + 1), y + h * (3 + b)), clr, -1)
        elif s == 1:
            cv2.rectangle(frame, (x + w * a, y + h * (2 + b)), (x + w * (a + 2), y + h * (3 + b)), clr, -1)
        else:
            cv2.rectangle(frame, (x + w * a, y + h * (2 + b)), (x + w * (a + 1), y + h * (4 + b)), clr, -1)
        ab = ""

    # DRAW CALC
    frame = my.draw_calc(frame, 15, -10)

    # FIND CONTOURS
    contours, hararky = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:

        # FIND CONTOUR OF MAX AREA WHICH IS CONTOUR OF HAND
        contour = max(contours, key=lambda x: cv2.contourArea(x))
        hull = cv2.convexHull(contour)
        approx = cv2.approxPolyDP(hull, 0.01 * cv2.arcLength(hull, True), True)

        # DRAW APPROX POLYGON OF HAND
        # cv2.drawContours(roi, [approx], 0, (0, 0, 255))

        # DRAW SMALL CIRCLE ON TIP OF FINGER
        roi = my.detect_finger(roi, approx)

        # CHECK FOR CLICK
        a, b = my.check_event(approx, prev_approx)

        # IF CLICK UPDATE ANSWER FOR DISPLAY BOARD
        if b < 590:
            ans, ab = my.press_key(ans, a, b)
            # print(ans)
            if ans == "quit":
                cap.release()

            # DRAW CIRCLE WHERE CLICKED
            cv2.circle(roi, (a, b), 5, (255, 0, 0), 2)

        # STORE APPROX ARRAY FOR NEXT FRAME
        prev_approx = approx

    except:
        # print("pass")

        # LITTLE BIT TRICKEY THINK ABOUT IT
        # IT IS NECESSARY
        prev_approx = approx

    # MAKE ANSWER LONG ENOUGH TO DISPLAY ON DISPLAY BOARD
    l = len(ans)
    if l > 10:
        ans1 = ans[l - 9:l]
        ans1 = "..." + ans1
    else:
        ans1 = ans

    # WRITE ON DISPLAY BOARD
    cv2.putText(frame, ans1, (x + int(w * 0.15), y + int(h * 0.7)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # frame = cv2.resize(frame, (800, 600))
    thres = cv2.resize(thres, (120, 120))
    cv2.imshow("frame", frame)
    cv2.imshow("roi", thres)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
