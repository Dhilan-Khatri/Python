import cv2, time, pyautogui
import mediapipe as mp
mpHands=mp.solutions.hands
mpDraw=mp.solutions.drawing_utils
hands=mpHands.hands(max_num_hands=1, min_detection_confidence=0.6)
scrollSpeed=400
scrollDelay=0.25
camHeight,camWidth=400,500
def gestureDetecting(landmarks, handedness):
    tips=[mpHands.HandLandmark.INDEX_FINGER_TIP, mpHands.HandLandmark_MIDDLE_FINGER_TIP, mpHands.HandLandmark_RING_FINGER_TIP, mpHands.HandLandmark.PINKY_FINGER_TIP]
    thumbTip=landmarks.landmark[mpHands.HandLandmark.THUMB_TIP]
    thumbIp=landmarks.landmark[mpHands.HandLandmark.THUMB_ID]
    finger=[]
    for tipIndex in tips:
        if landmarks.landmark[tipIndex].y<landmarks.landmark[tipIndex-2].y:
            finger.append(1)
        if (handedness=="Right" and thumbTip>thumbIp) or (handedness=="Left" and thumbTip<thumbIp):
            finger.append(1)
        return "scrollUp" if sum(finger)==5 else "scrollDown" if sum(finger)==0 else "None"
cap=cv2.VideoCapture(0)
cap.set(3,camWidth)
cap.set(3,camHeight)
lastscroll,ptime=0
print("Gesture Control:\n Open Fist : Scroll Up\n Closed Fist : Scroll Down\n q : Quit")
while cap.isOpened():
    success,img=cap.read()
    if not success:
        break
    img=cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
    results=hands.process(img)
    gesture="None"
    handedness="Unknown"
    if results.multi_hand_landmarks:
        for hand, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness=handedness_info.classification[0].label
            gesture=gestureDetecting(hand,handedness)
            mpDraw.draw_landmarks(img,hand,mpHands.HAND_CONNECTIONS)
            if (time.time()-lastscroll)>scrollDelay:
                if gesture=="scrollUp": pyautogui.scroll(scrollSpeed)
                elif gesture=="scrollDown": pyautogui.scroll(-scrollSpeed)
                lastscroll=time.time()
    fps=1/(time.time()-ptime) if (time.time()-ptime)>0 else 0
    ptime=time.time()
    cv2.putText(img,f"FPS : {int(fps)}, Hand : {handedness}, Gesture : {gesture}", (10,30),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7, (255,0,0),2 )
    cv2.imshow("Gesture Control", cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()