import cv2
import numpy as n
import matplotlib.pyplot as p

def applyFilter(image,filtertype):
    filteredImage=image.copy()
    if filterType=="red_tint":
        filteredImage[:,:,1]=0 #Green Channel to 0
        filteredImage[:,:,0]=0 #Blue Channel to 0
    elif filterType=="green_tint":
        filteredImage[:,:,2]=0 #Red Channel to 0
        filteredImage[:,:,0]=0 #Blue Channel to 0
    elif filterType=="blue_tint":
        filteredImage[:,:,2]=0 #Red Channel to 0
        filteredImage[:,:,1]=0 #Green Channel to 0 
    elif filterType=="increase_red":
        filteredImage[:,:,2]=cv2.add(filteredImage[:,:,2],50) #Increase Red Channel
    elif filterType=="decrease_blue":
        filteredImage[:,:,0]=cv2.subtract(filteredImage[:,:,0],50) #Decrease blue Channel
    return filteredImage

image=cv2.imread("example.jpg")
if image is None:
    print("Error: Image Not Found")
else: 
    image=cv2.resize(image, (800,600))
    filterType="Orginal"
    print("Press the Following Keys to Apply the Filter:")
    print("r- Red Tint")
    print("g- Green Tint")
    print("b- Blue Tint")
    print("i- Increase Red Intensity")
    print("d- Decrease Blue Intensity")
    print("q- Quit")

    while True:
        filterImage=applyFilter(image,filterType)
        cv2.imshow("Filtered Image", filterImage)
        key=cv2.waitKey(0) & 0xFF
        if key==ord("r"):
            filterType="red_tint"
        elif key==ord("g"):
            filterType="green_tint"
        elif key==ord("b"):
            filterType="blue_tint"
        elif key==ord("i"):
            filterType="increase_red"
        elif key==ord("d"):
            filterType="decrease_blue"
        elif key==ord("q"):
            print("Quiting...")
            break
        else:
            print("Invaid Key Use: Please Use (r/g/b/i/d/q)")
cv2.destoryAllWindows()
