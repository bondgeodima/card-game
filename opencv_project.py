import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    # Capture frame-by-frame
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break
