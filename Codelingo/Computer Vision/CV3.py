import cv2
image=cv2.imread("download.jfif")
greyimage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resizedImage1=cv2.resize(greyimage,(250,250))
cv2.imshow("Processed Image", resizedImage1)
key=cv2.waitKey(0)
if key==ord("S"):
    cv2.imwrite("greyimage.jpg", resizedImage1)
    print("Image Saved As 'greyimage.jpg'")
else:
    print("Image Not Saved")
cv2.destroyAllWindows()
print(f"Processed Image Dimessions: {resizedImage1.shape}")

resizedImage2=cv2.resize(greyimage,(300,300))
cv2.imshow("Processed Image", resizedImage2)
key=cv2.waitKey(0)
if key==ord("S"):
    cv2.imwrite("greyimage.jpg", resizedImage2)
    print("Image Saved As 'greyimage.jpg'")
else:
    print("Image Not Saved")
cv2.destroyAllWindows()
print(f"Processed Image Dimessions: {resizedImage2.shape}")

resizedImage3=cv2.resize(greyimage,(200,200))
cv2.imshow("Processed Image", resizedImage3)
key=cv2.waitKey(0)
if key==ord("S"):
    cv2.imwrite("greyimage.jpg", resizedImage3)
    print("Image Saved As 'greyimage.jpg'")
else:
    print("Image Not Saved")
cv2.destroyAllWindows()
print(f"Processed Image Dimessions: {resizedImage3.shape}")