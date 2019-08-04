"""
================================
Recognizing hand-written digits
================================

This lets you click through the images in the digit library.

"""
print(__doc__)


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

offset = 0

def onclick(event):
    global offset
    plt.clf()
    offset += total_digits
    print "Redrawing digit table from %d to %d" % (offset, offset + total_digits)
    draw_digit_table(offset, offset + total_digits)


def draw_digit_table(from_index, to_index):
    for index, (image, label) in enumerate(images_and_labels[from_index:to_index]):
        # num rows, num cols, index.
        plt.subplot(num_rows, num_cols, index + 1)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        
        # plt.title('%d: %i' % (offset + index, label))
        plt.title('%d' % (offset + index))

    plt.show()


fig,ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', onclick)

draw_digit_table(offset, offset + total_digits)






