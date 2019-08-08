"""
================================
Recognizing hand-written digits
================================

Predict a single handwritten digit.
"""

import cv2
import numpy as np





import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random import randrange

from numpy import array
from numpy import uint8

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

########
# CONVERT IMAGE
########

img_path = './digit2.jpeg'
img = cv2.imread(img_path, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 

# print img
img_reverted= cv2.bitwise_not(img)
# print img_reverted

# now all values are ranging from 0 to 15, where white equlas 0 and black equals 15 
new_img = img_reverted / 16  

print repr(new_img)



# The digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# PREDICT_DATA = data[INDEX_TO_PREDICT] 

# print "DIGIT ARRAY IMAGE"
# print digits.images[INDEX_TO_PREDICT]


## predrawn digit
DRAWN_DIGIT = new_img
# DRAWN_DIGIT = array([[ 0,  0,  0,  0,  0,  0,  0,  0],
#        [ 0,  0,  9, 12, 10, 11,  0,  0],
#        [ 0,  0, 15,  0,  0,  0,  0,  0],
#        [ 0,  0, 12, 12, 15,  2,  0,  0],
#        [ 0,  0,  0,  0,  0, 15,  0,  0],
#        [ 0,  0,  2,  0,  0,  9,  0,  0],
#        [ 0,  0, 10, 12, 12, 10,  0,  0],
#        [ 0,  0,  0,  0,  0,  0,  0,  0]], dtype=uint8)

# DRAWN_DIGIT = array([[ 0,  0,  1,  5,  3,  0,  0,  0],
#        [ 0,  4, 11,  5, 11,  1,  0,  0],
#        [ 0,  7,  1,  0,  7,  2,  0,  0],
#        [ 0,  0,  0,  0,  8,  3,  0,  0],
#        [ 0,  0,  0,  6,  9,  1,  0,  0],
#        [ 0,  5,  8,  5,  0,  0,  0,  0],
#        [ 2, 15,  9,  5,  5,  5,  5,  5],
#        [ 1,  5,  4,  4,  4,  4,  4,  4]], dtype=uint8)

print DRAWN_DIGIT
print DRAWN_DIGIT.shape

# flatten into 1D ARRAY
PREDICT_DATA = DRAWN_DIGIT.reshape((1,-1))[0]

print "DIGITA ARRAY FLATTENED"
print PREDICT_DATA

# Now predict the value of the digit on the second half:
# expected = digits.target[n_samples // 2:]
predicted = classifier.predict([PREDICT_DATA])
print "PREDICTION"
print predicted

plt.subplot(1, 1, 1)
# plt.axis('off')
plt.imshow(DRAWN_DIGIT, cmap=plt.cm.gray_r, interpolation='nearest')

plt.show()
