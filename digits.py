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

num_rows = 10
num_cols = 10
total_digits = num_rows * num_cols

for index, (image, label) in enumerate(images_and_labels[:num_rows * num_cols]):
    # num rows, num cols, index.
    # plt.subplot(num_rows, num_cols, 1)
    plt.subplot(1,1,1)

    # plt.subplot(num_rows, num_cols, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('T: %i' % label)
    plt.pause(0.1)
    plt.clf()

# plt.show()

# time.sleep(1000)
# plt.clear()


# # To apply a classifier on this data, we need to flatten the image, to
# # turn the data in a (samples, feature) matrix:
# n_samples = len(digits.images)
# data = digits.images.reshape((n_samples, -1))

# # Create a classifier: a support vector classifier
# classifier = svm.SVC(gamma=0.001)

# # We learn the digits on the first half of the digits
# classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# # Now predict the value of the digit on the second half:
# expected = digits.target[n_samples // 2:]
# predicted = classifier.predict(data[n_samples // 2:])

# print("Classification report for classifier %s:\n%s\n"
#       % (classifier, metrics.classification_report(expected, predicted)))
# print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

# images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
# # for index, (image, prediction) in enumerate(images_and_predictions[:4]):

# for index, (image, prediction) in enumerate(images_and_predictions[10:14]):
#     plt.subplot(2, 4, index + 5)
#     plt.axis('off')
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.title('Prediction: %i' % prediction)

