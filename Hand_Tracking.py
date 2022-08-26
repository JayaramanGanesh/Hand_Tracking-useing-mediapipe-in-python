import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hand = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
while True:
    ret,frame = cap.read()
    colour = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hand.process(colour)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame,handlms,mphands.HAND_CONNECTIONS)
            
    cv2.imshow("frame",frame)
    cv2.waitKey(1)
    