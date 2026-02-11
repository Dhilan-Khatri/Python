import cv2
image=cv2.imread("download.jfif")
greyimage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resizedImage=cv2.resize(greyimage,(224,224))
cv2.imshow("Processed Image", resizedImage)
key=cv2.waitKey(0)
if key==ord("S"):
    cv2.imwrite("greyimage.jpg", resizedImage)
    print("Image Saved As 'greyimage.jpg'")
else:
    print("Image Not Saved")
cv2.destroyAllWindows()
print(f"Processed Image Dimessions: {resizedImage.shape}")