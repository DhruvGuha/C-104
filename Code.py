import cv2

img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
img[100:340,0:100] = rocket
cv2.imshow("Rocket",img)
# gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imshow("Rocket2",gray_img)
cv2.waitKey(0)