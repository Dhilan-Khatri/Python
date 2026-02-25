import cv2
import matplotlib.pyplot as p
import numpy as n
image=cv2.imread("download.jfif")
imageRGB=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Rotate Image 45 degrees
(h,w)=image.shape[:2]
center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image,m,(w,h))
rotatedImageRBG=cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
p.imshow(rotatedImageRBG)
p.title("Rotated Image")
p.show()

#Brightness
brightnessMatrix=n.ones(image.shape,dtype="uint8")*50
brighter=cv2.add(image,brightnessMatrix)
brighterImageRBG=cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
p.imshow(brighterImageRBG)
p.title("Brighter Image")
p.show()