from PIL import Image
import cv2

file = input("Enter file name:")
img = cv2.imread(file)

dimensions = img.shape

height = img.shape[0]
width = img.shape[1]

dsize = (width,height)

img_canvas = cv2.imread("canvas.jpg")
img_canvas1 = cv2.resize(img_canvas,dsize)
img2 = cv2.multiply(img, img_canvas1, scale=1/512)
img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img_invert = 255-img_gray
img_gauss = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

final_img = dodgeV2(img_gray, img_gauss)

cv2.imwrite(file + "_final.jpg", final_img)

cv2.imshow('image',final_img)
cv2.waitKey(0)
