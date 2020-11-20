import cv2
import numpy as np


def thresold(roi):
    # READ HSV VALUES FROM FILE
    hsv_values = np.loadtxt('data/hsv_values.txt', dtype=int)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi = cv2.inRange(roi, hsv_values[0], hsv_values[1])

    return roi




def draw_calc(frame, a, b):
    values = np.loadtxt('data/values.txt', int)

    x = values[0]
    y = values[1]
    h = values[2]
    w = values[3]

    color = (255, 0, 0)

    cv2.line(frame, (x, y), (x, y + h * 8), color, 2)
    cv2.line(frame, (x + w, y + h * 2), (x + w, y + h * 7), color, 2)
    cv2.line(frame, (x + w * 2, y + h * 2), (x + w * 2, y + h * 8), color, 2)
    cv2.line(frame, (x + w * 3, y + h * 2), (x + w * 3, y + h * 8), color, 2)
    cv2.line(frame, (x + w * 4, y), (x + w * 4, y + h * 8), color, 2)

    cv2.line(frame, (x, y), (x + w * 4, y), color, 2)
    cv2.line(frame, (x, y + h * 2), (x + w * 4, y + h * 2), color, 2)
    cv2.line(frame, (x, y + h * 3), (x + w * 4, y + h * 3), color, 2)
    cv2.line(frame, (x, y + h * 4), (x + w * 4, y + h * 4), color, 2)
    cv2.line(frame, (x, y + h * 5), (x + w * 3, y + h * 5), color, 2)
    cv2.line(frame, (x, y + h * 6), (x + w * 4, y + h * 6), color, 2)
    cv2.line(frame, (x, y + h * 7), (x + w * 3, y + h * 7), color, 2)
    cv2.line(frame, (x, y + h * 8), (x + w * 4, y + h * 8), color, 2)

    cv2.putText(frame, "C", (x + a, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "^", (x + w + a, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "_", (x + 2 * w + a, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "..", (x + 3 * w + a, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "%", (x + 0 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "/", (x + 1 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "*", (x + 2 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "-", (x + 3 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "7", (x + 0 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "8", (x + 1 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "9", (x + 2 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "4", (x + 0 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "5", (x + 1 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "6", (x + 2 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "1", (x + 0 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "2", (x + 1 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "3", (x + 2 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, " .", (x + 2 * w + a, y + 8 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "0", (x + int(0.5 * w) + a, y + 8 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "+", (x + 3 * w + a, y + int(5.5 * h) + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "=", (x + 3 * w + a, y + int(7.5 * h) + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

    return frame


def detect_finger(roi, arr):
    if 5 <= arr.shape[0] <= 7:
        for a in arr:
            if a[0, 1] < 590:
                cv2.circle(roi, (a[0, 0], a[0, 1]), 5, (0, 255, 0), 2)
        return roi


def check_event(approx, prev_approx):
    if 5 <= prev_approx.shape[0] <= 7 & prev_approx.shape[0] == approx.shape[0] + 1:
        for i in range(prev_approx.shape[0]):
            l = True
            for j in range(approx.shape[0]):
                a = abs(prev_approx[i, 0, 0] - approx[j, 0, 0])
                b = abs(prev_approx[i, 0, 1] - approx[j, 0, 1])
                if a * a + b * b < 401:
                    l = False
                    break
            if l:
                return prev_approx[i, 0, 0], prev_approx[i, 0, 1]
        return 0, 600
    else:
        return 0, 600


def calc(ans):
    a, b, y = "", "", ""
    c = 0
    for x in ans:
        if c == 0 and (
                x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "." or x == "0"):
            a += x
        elif x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "." or x == "0":
            b += x
        else:
            y = x
            c = 1

    bb = b
    a = float(a)
    if len(b) != 0:
        b = float(b)
    if len(y) == 0:
        return ans
    elif len(bb) == 0:
        return ""
    elif y == "^":
        a **= b
    elif y == "%":
        a %= b
    elif y == "/":
        a /= b
        a = round(a, 5)
    elif y == "*":
        a *= b
    elif y == "-":
        a -= b
    elif y == "+":
        a += b
    else:
        pass

    ans = str(a)
    return ans


def press_key(ans, a, b):
    values = np.loadtxt('data/values.txt', int)
    ab = ""
    x = values[0]
    y = values[1]
    h = values[2]
    w = values[3]
    a = a + 400
    if x < a < x + 4 * w and y + 2 * h < b < y + 8 * h:
        a -= x
        a /= w
        b -= y
        b /= h
        b -= 2
        a = int(a)
        b = int(b)
        if a == 0 and b == 0:
            ans = ""
            ab = "000"
        elif a == 1 and b == 0:
            ans = calc(ans)
            ans += "^"
            ab = "100"
        elif a == 2 and b == 0:
            ans = ans[:len(ans) - 1]
            ab = "200"

        elif a == 3 and b == 0:
            ans = "quit"
            ab = "300"

        elif a == 0 and b == 1:
            ans = calc(ans)
            ans += "%"
            ab = "010"
        elif a == 1 and b == 1:
            ans = calc(ans)
            ans += "/"
            ab = "110"
        elif a == 2 and b == 1:
            ans = calc(ans)
            ans += "*"
            ab = "210"
        elif a == 3 and b == 1:
            ans = calc(ans)
            ans += "-"
            ab = "310"

        elif a == 0 and b == 2:
            ans += "7"
            ab = "020"
        elif a == 1 and b == 2:
            ans += "8"
            ab = "120"
        elif a == 2 and b == 2:
            ans += "9"
            ab = "220"
        elif a == 3 and b == 2:
            ans = calc(ans)
            ans += "+"
            ab = "322"

        elif a == 0 and b == 3:
            ans += "4"
            ab = "030"
        elif a == 1 and b == 3:
            ans += "5"
            ab = "130"
        elif a == 2 and b == 3:
            ans += "6"
            ab = "230"
        elif a == 3 and b == 3:
            ans = calc(ans)
            ans += "+"
            ab = "332"

        elif a == 0 and b == 4:
            ans += "1"
            ab = "040"
        elif a == 1 and b == 4:
            ans += "2"
            ab = "140"
        elif a == 2 and b == 4:
            ans += "3"
            ab = "240"
        elif a == 3 and b == 4:
            ans = calc(ans)
            ab = "342"

        elif a == 0 and b == 5:
            ans += "0"
            ab = "051"
        elif a == 1 and b == 5:
            ans += "0"
            ab = "151"
        elif a == 2 and b == 5:
            ans += "."
            ab = "250"
        elif a == 3 and b == 5:
            ans = calc(ans)
            ab = "352"
        else:
            pass

        return ans, ab
    else:
        return ans, ab
