import cv2
import matplotlib.pyplot as p
image=cv2.imread("example.jpg")
imageRGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_=imageRGB.shape

#Rectangle
rectangle1Width,rectangle1Height=150,150
topLeft=(20,20)
bottomRight=(topLeft[0]+rectangle1Width,topLeft[1]+rectangle1Height)
cv2.rectangle(imageRGB,topLeft,bottomRight,(0,255,255),3)
rectangle2Width,rectangle2Height=200,150
topLeft2=(width-rectangle2Width-20,height-rectangle2Height-20)
bottomRight2=(topLeft2[0]+rectangle2Width,topLeft2[1]+rectangle2Height)
cv2.rectangle(imageRGB,topLeft2,bottomRight2,(255,0,255),3)

#Circle
center1x=topLeft[0]+rectangle1Width//2
center1y=topLeft[1]+rectangle1Height//2
center2x=topLeft2[0]+rectangle2Width//2
center2y=topLeft2[1]+rectangle2Height//2
cv2.circle(imageRGB, (center1x,center1y), 15,(0,255,0),-1)
cv2.circle(imageRGB, (center2x,center2y), 15,(0,255,0),-1)

#Line
cv2.line(imageRGB,(center1x,center1y),(center2x,center2y),(255,0,0),3)

#Arrow
arrowStart=(width-50,20)
arrowEnd=(width-50,height-20)
cv2.arrowedLine(imageRGB,arrowStart,arrowEnd,(255,255,255),3,tipLength=0.05)
cv2.arrowedLine(imageRGB,arrowEnd,arrowStart,(255,255,255),3,tipLength=0.05)
heightLabelPostion=(arrowStart[0]-150,(arrowStart[1]+arrowEnd[1]//2))
# Horizontal Width Arrow
widthArrowStart = (20, height - 50)
widthArrowEnd = (width - 20, height - 50)

cv2.arrowedLine(imageRGB, widthArrowStart, widthArrowEnd, (255, 255, 255), 3, tipLength=0.05)
cv2.arrowedLine(imageRGB, widthArrowEnd, widthArrowStart, (255, 255, 255), 3, tipLength=0.05)

# Width Label Position
widthLabelPosition = ((widthArrowStart[0] + widthArrowEnd[0]) // 2 - 60, height - 60)

#Text Labels
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imageRGB,"Region 1", (topLeft[0],topLeft[1]-5),font,0.7,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imageRGB,"Region 2", (topLeft2[0],topLeft2[1]-5),font,0.7,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imageRGB,"Center 1", (center1x-40,center1y-40),font,0.6,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imageRGB,"Center 2", (center2x-40,center2y+40),font,0.6,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imageRGB,f"Height:{height}px", (heightLabelPostion),font,0.6,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imageRGB,f"Width: {width}px",widthLabelPosition,font,0.6,(0, 0, 0),2,cv2.LINE_AA)

p.figure(figsize=(12,8))
p.imshow(imageRGB)
p.title("Annotation Image With Region, Centers, and Bidirectional")
p.axis("off")
p.show()