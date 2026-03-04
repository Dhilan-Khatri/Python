import cv2
import numpy as n
import matplotlib.pyplot as p

def displayImage(title,image):
    p.figure(figsize=(8,8))
    if len(image.shape)==2:
        p.imshow(image,cmap="grey")
    else:
        p.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    p.title(title)
    p.axis("off")
    p.show()
def interactiveEdgeDetection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("Error: Image Not Found")
        return
    greyImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    displayImage("Orginal Greyscale Image", greyImage)
    print("Select An Option")
    print("1. SOBEL Edge Detection\n 2. CANNY Edge Detection\n 3. LAPLACIAN Edge Detection\n 4. GAUSSIAN Smoothing \n 5. Median Filtering\n 6. Exit")
    while True:
        choice=input("Your Choice (1-6): ")
        if choice=="1":
            SOBEL_X=cv2.Sobel(greyImage, cv2.CV_64F, 1, 0, ksize=3)
            SOBEL_Y=cv2.Sobel(greyImage, cv2.CV_64F, 0, 1, ksize=3)
            combineSOBEL=cv2.bitwise_or(SOBEL_X.astype(n.uint8),SOBEL_Y.astype(n.uint8))
            displayImage("SOBEL Edge Detection", combineSOBEL)
        elif choice=="2":
            print("Adjust Thureshold For CANNY, Default:100&200")
            lowerThureshold=int(input("Enter Lower Thureshold: "))
            higherThureshold=int(input("Enter Higher Thureshold: "))
            edges=cv2.Canny(greyImage,lowerThureshold,higherThureshold)
            displayImage("CANNY Edge Detection", edges)
        elif choice=="3":
            LAPLACIAN=cv2.Laplacian(greyImage,cv2.CV_64F)
            displayImage("LAPLACIAN Edge Detection", n.abs(LAPLACIAN).astype(n.uint8))
        elif choice=="4":
            print("Adjust Size For GAUSSIAN Blur (Default=5)")
            size=int(input("Enter Size (Odd Number): "))
            blur=cv2.GaussianBlur(image,(size,size),0)
            displayImage("GAUSSIAN Smoothing", blur)
        elif choice=="5":
            print("Ajust Size for Median Filtering (Default=5)")
            size=int(input("Enter Size (Odd Number): "))
            filter=cv2.medianBlur(image,size)
            displayImage("Median Filter Image", filter)
        elif choice=="6":
            print("Exiting")
            break
        else:
            print("Invalid Choice, Please Input An Number Between 1-6")
interactiveEdgeDetection("example.jpg")