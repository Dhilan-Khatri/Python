import cv2
import matplotlib.pyplot as p
image=cv2.imread("download.jfif")

#Changing Color
imageRGB=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
p.imshow(imageRGB)
p.title("RGB Images")
p.show()
imageGRAY=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
p.imshow(imageGRAY, cmap="gray")
p.title("Gray Images")
p.show()

#Cropping Images
croppedImage=image[0:50, 50:100]
croppedImageRGB=cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
p.imshow(croppedImageRGB)
p.title("Cropped RGB Images")
p.show()