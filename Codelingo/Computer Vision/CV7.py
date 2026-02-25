import cv2
import matplotlib.pyplot as p
import numpy as n

image=cv2.imread("download.jfif")
imageRGB=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image2=cv2.imread("download2.jfif")
imageRGB2=cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
image3=cv2.imread("download3.jfif")
imageRGB3=cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
#image 1
(h,w)=image.shape[:2]
center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image,m,(w,h))
rotatedImageRBG=cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
p.imshow(rotatedImageRBG)
p.title("Rotated Image")
p.show()
brightnessMatrix=n.ones(image.shape,dtype="uint8")*50
brighter=cv2.add(image,brightnessMatrix)
brighterImageRBG=cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
p.imshow(brighterImageRBG)
p.title("Brighter Image")
p.show()
croppedImage=image[0:50, 50:100]
croppedImageRGB=cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
p.imshow(croppedImageRGB)
p.title("Cropped RGB Images")
p.show()
#image 2
(h,w)=image2.shape[:2]
center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image2,m,(w,h))
rotatedImageRBG=cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
p.imshow(rotatedImageRBG)
p.title("Rotated Image")
p.show()
brightnessMatrix=n.ones(image2.shape,dtype="uint8")*50
brighter=cv2.add(image2,brightnessMatrix)
brighterImageRBG=cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
p.imshow(brighterImageRBG)
p.title("Brighter Image")
p.show()
croppedImage=image2[0:50, 50:100]
croppedImageRGB=cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
p.imshow(croppedImageRGB)
p.title("Cropped RGB Images")
p.show()
#image 3
(h,w)=image3.shape[:2]
center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image3,m,(w,h))
rotatedImageRBG=cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
p.imshow(rotatedImageRBG)
p.title("Rotated Image")
p.show()
brightnessMatrix=n.ones(image3.shape,dtype="uint8")*50
brighter=cv2.add(image3,brightnessMatrix)
brighterImageRBG=cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
p.imshow(brighterImageRBG)
p.title("Brighter Image")
p.show()
croppedImage=image3[0:50, 50:100]
croppedImageRGB=cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
p.imshow(croppedImageRGB)
p.title("Cropped RGB Images")
p.show()