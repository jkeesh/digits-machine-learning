import cv2
import numpy as np

img_path = './digit2.jpeg'
img = cv2.imread(img_path, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 

# print img
img_reverted= cv2.bitwise_not(img)
# print img_reverted

# now all values are ranging from 0 to 15, where white equlas 0 and black equals 15 
new_img = img_reverted / 16  

print repr(new_img)

