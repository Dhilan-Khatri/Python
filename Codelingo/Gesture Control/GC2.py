import cv2, time, pyautogui
import mediapipe as mp
import numpy
mpHands=mp.solutions.hands
hands=mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw=mp.solutions.drawing_utils
scrollSpeed=300
scrollDelay=1
camWidth=640
camHeight=480
def detectGesture(landmarks, handedness):
    fingers=[]
    tips=[mpHands.HandLandmark.INDEX_FINGER_TIP,mpHands.HandLandmark.MIDDLE_FINGER_TIP,mpHands.HandLandmark.RING_FINGER_TIP,mpHands.HandLandmark.PINKY_TIP]
    for tipIndex in tips:
        if landmarks.landmark[tipIndex].y<landmarks.landmark[tipIndex-2].y:
            fingers.append(1)
    thumbTip=landmarks.landmark[mpHands.HandLandmark.THUMB_TIP]
    thumbIp=landmarks.landmark[mpHands.HandLandmark.THUMB_IP]
    if (handedness=="Right" and thumbTip.x>thumbIp.x) or (handedness=="Left" and thumbTip.x<thumbIp.x):
        fingers.append(1)
    return "scroll_Up" if sum(fingers)==5 else "scroll_Down" if len(fingers)==0 else "None"
cap=cv2.VideoCapture(0)
