import cv2
import mediapipe as mp
mpHands=mp.solutions.hands
hands=mpHands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
mpDraw=mp.solutions.drawing_utiles
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Can Not Acess Webcame")
    exit()
print("Hand Tracking Started; Press 'q' To Quit")
def detectGesture(handLandMarks):
    landMarks=handLandMarks.landmark()
    tipIDs=[4,8,12,16,20]
    pipIDs=[2,4,10,14,18]
    extended=0
    if abs(landMarks[tipIDs[0]].x-landMarks[pipIDs[0]].x)>0.04:
        extended+=1
    for i in range(1,5):
        if landMarks[tipIDs[0]].y<landMarks[pipIDs[0]].y:
            extended+=1
    if extended>=4:
        return "Open"
    elif extended<=1:
        return "Closed Fist"
    else:
        return "Partial"
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    h,w,_=frame.shape()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hands.process(frameRGB)
    gesture="No-Hand"
    if result.multi_hand_landmarks and result.multiHandedness:
        for index,handlandmarks in enumerate(result.multi_hand_landmarks):
            handLabel=result.multi_handedness[index].classifcation[0].label
            gesture=detectGesture(handlandmarks)
            mp_draw.draw_landmarks(frame,handlandmarks,mp_hands.HAND_CONNECTIONS)
            fingertipsIDs=[4,8,12,16,20]
            for tipid in fingertipsIDs:
                l=handlandmarks.landmark[tipid]
                x,y=int(l.x*w), int(l.y*h)
                cv2.circle(frame,(x,y),10,(255,0,255),cv2.FILL)
                cv2.putText(frame,str(tipid),(x-5,y-15))
            wrist=handlandmarks.landmark[0]
            xWrist,yWrist=int(wrist.x*w), int(wrist.y*h)
            cv2.putText(frame,f"{handLabel} hands",(xWrist-40,yWrist+30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    statusColor=(0,255,0) if gesture in ["Open", "Closed Fist"] else (0,165,265)
    cv2.putText(frame,f"gesture: {gesture}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.imshow("Hand Gesture Detected", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()