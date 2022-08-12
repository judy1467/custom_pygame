import cv2, os

image_gray = cv2.imread('resources/images/map/map1.jpg', cv2.IMREAD_GRAYSCALE)

file_list = os.listdir('resources/images/map/')
print(file_list)

blur = cv2.GaussianBlur(image_gray, ksize=(3,3), sigmaX=0)
ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
edged = cv2.Canny(blur, 10, 250)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('resources/convert/convert-1.jpg', closed)
cv2.imshow('closed', closed)
cv2.waitKey(0)
cv2.destroyAllWindows()