import cv2
import numpy as np
import matplotlib.pyplot as plt
def applyFilter(image, fType):
    img=image.copy()
    if fType=="Red":
        img[:,:,1]=0
        img[:,:,0]=0
    elif fType=="Blue":
        img[:,:,1]=0
        img[:,:,2]=0
    elif fType=="Green":
        img[:,:,0]=0
        img[:,:,2]=0
    elif fType=="Sobel":
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        x=cv2.Sobel(gray, cv2.CV_64F,1,0,ksize=3)
        y=cv2.Sobel(gray, cv2.CV_64F,0,1,ksize=3)
        sob=cv2.bitwise_or(x.astype("uint8"),y.astype("uint8"))
        img=cv2.cvtColor(sob,cv2.COLOR_GRAY2BGR)
    elif fType=="Canny":
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        c=cv2.Canny(gray,100,200)
        img=cv2.cvtColor(c,cv2.COLOR_GRAY2BGR)
    elif fType=="Cartoon":
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color=cv2.bilateralFilter(image,9,300,300)
        img=cv2.bitwise_and(color,color,mask=edges)
    return img
def main():
    v=cv2.VideoCapture(0)
    if not v.isOpened():
        print("Error: Can Not Open Camera Feed")
        return
    else:
        fType="Orginal"
        print("East: R=Red, B=Blue, G=Green, S=SOBEL, C=CANNY, T=Cartoon, q=quit")
        while True:
            ret,frame=v.read()
            if not ret:
                print("Error: Cannot Open See Frame")
                return
            out=applyFilter(frame, fType)
            cv2.imshow("Video Feed", out)
            key=cv2.waitKey(1) & 0xFF
            if key==ord("r"):
                fType="Red"
            if key==ord("b"):
                fType="Blue"
            if key==ord("g"):
                fType="Green"
            if key==ord("s"):
                fType="Sobel"
            if key==ord("c"):
                fType="Canny"
            if key==ord("t"):
                fType="Cartoon"
            if key==ord("q"):
                break
        v.release()
        cv2.destoryAllWindows()
main()