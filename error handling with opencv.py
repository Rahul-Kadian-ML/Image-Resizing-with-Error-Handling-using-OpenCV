import cv2
try:
    img=cv2.imread('download.jpeg')
    print(img)
    if img is None:
       raise FileNotFoundError("Image not found")
except FileNotFoundError as e:
    print(e)
    print("Image is not found")
else:
    resized=cv2.resize(img,(500,400))
    cv2.imshow("Resized:",resized)
    cv2.waitKey(0)
    print("Image is found")
finally:
    cv2.destroyAllWindows()
    print("End program")