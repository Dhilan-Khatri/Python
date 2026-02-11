import cv2
image=cv2.imread("download.jfif")
cv2.namedWindow("loadedImage", cv2.WINDOW_NORMAL)
cv2.resizeWindow("loadedImage", 800,500)
cv2.imshow("loadedImage", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image Dimension {image.shape}")
