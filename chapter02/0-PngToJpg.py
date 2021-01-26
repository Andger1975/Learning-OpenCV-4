import cv2

image = cv2.imread('MyPic.png')
cv2.imwrite('MyPic1.jpg', image)
print(image)

