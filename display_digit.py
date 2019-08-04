print(__doc__)

# Import libraries

from sklearn import datasets

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Load the digits dataset
digits = datasets.load_digits()

# index = input("Enter index: ")
# print index

# DIGIT_INDEX = index
DIGIT_INDEX = 0
print digits.images[DIGIT_INDEX]

#Display the first digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[DIGIT_INDEX], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()


