import cv2
emoji=cv2.imread("HappyEmoji.jfif")
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
captureFootage=cv2.VideoCapture(0) # 0=Default Camera   1=External Camera
if not captureFootage.isOpened():
    print("Error: Camera Not Opened")
    exit()
while True:
    ret,frame=captureFootage.read()
    if not ret:
        print("Error: Failed To Capture Image")
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5,minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+w),(255,0,0),2)
        emojiResized=cv2.resize(emoji,(w,h))
        frame[y:y+h, x:x+w]=emojiResized
    cv2.imshow("Face Detection (Press q to Quit)",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
captureFootage.release()
cv2.destroyAllWindows()