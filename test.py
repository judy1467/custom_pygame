import cv2, os
from PIL import Image

file_list = os.listdir('resources/images/map/')
print(file_list)

for map in file_list:
    image_gray = cv2.imread('resources/images/map/'+map, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(image_gray, ksize=(3,3), sigmaX=0)
    ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
    edged = cv2.Canny(blur, 10, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    cv2.imwrite('resources/convert/'+map, closed)

file_list = os.listdir('resources/convert/')

for map in file_list:
    img = Image.open('resources/convert/'+map)

    img_resize = img.resize((570, 520))
    img_resize.save('resources/convert/'+map)

    # img_resize_lanczos = img.resize((256, 256), Image.LANCZOS)
    # img_resize_lanczos.save('data/dst/sample_pillow_resize_lanczos.jpg')