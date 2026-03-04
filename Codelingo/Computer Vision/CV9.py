import cv2
import numpy as np
def applyFilter(image, filterType):
    filteredImage = image.copy()
    if filterType == "red_tint":
        filteredImage[:, :, 1] = 0
        filteredImage[:, :, 0] = 0
    elif filterType == "green_tint":
        filteredImage[:, :, 2] = 0
        filteredImage[:, :, 0] = 0
    elif filterType == "blue_tint":
        filteredImage[:, :, 2] = 0
        filteredImage[:, :, 1] = 0
    elif filterType == "increase_red":
        filteredImage[:, :, 2] = cv2.add(filteredImage[:, :, 2], 50)
    elif filterType == "decrease_blue":
        filteredImage[:, :, 0] = cv2.subtract(filteredImage[:, :, 0], 50)
    return filteredImage
image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image Not Found")
else:
    image = cv2.resize(image, (800, 600))
    filterType = "original"
    print("Press Keys:")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("i - Increase Red")
    print("d - Decrease Blue")
    print("s - Save Image")
    print("q - Quit")
    while True:
        filteredImage = applyFilter(image, filterType)
        cv2.imshow("Filtered Image", filteredImage)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("r"):
            filterType = "red_tint"
        elif key == ord("g"):
            filterType = "green_tint"
        elif key == ord("b"):
            filterType = "blue_tint"
        elif key == ord("i"):
            filterType = "increase_red"
        elif key == ord("d"):
            filterType = "decrease_blue"
        elif key == ord("s"):
            filename = f"{filterType}_image.jpg"
            cv2.imwrite(filename, filteredImage)
            print(f"Image saved as '{filename}'")
        elif key == ord("q"):
            print("Quitting...")
            break
        else:
            print("Invalid key. Use r/g/b/i/d/s/q")
cv2.destroyAllWindows()