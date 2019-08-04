"""
================================
Recognizing hand-written digits
================================

An example showing how the scikit-learn can be used to recognize images of
hand-written digits.

This example is commented in the
:ref:`tutorial section of the user manual <introduction>`.

"""
print(__doc__)

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
# import matplotlib.pyplot as plt -- COMMENT OUT JBK

## NEEDED THIS UPDATE JBK
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# JBK
import time 

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

# print digits

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))

print "num in dataset: ", len(images_and_labels)

### THIS DEMO SHOWS A GRID OF SOME DIGITS

num_rows = 4
num_cols = 8
total_digits = num_rows * num_cols

def onclick(event):
    print(event.xdata, event.ydata)


# def draw_digit_table(from_index,)


fig,ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', onclick)


for index, (image, label) in enumerate(images_and_labels[:num_rows * num_cols]):
    # num rows, num cols, index.
    plt.subplot(num_rows, num_cols, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('T: %i' % label)

plt.show()





