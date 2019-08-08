# Digit recognition demo

## Quickstart

Download files.

    mkvirtualenv digits
    pip install -r reqs.txt

Run a program

    python display_digit.py

## Helpful python commands

Installing dependencies individually

    pip install scikit-learn
    pip install matplotlib

To return to virtual environment:

    workon digits

Running programs

    Display a single digit from the training data
    python display_digit.py

    Display a table of digits from the training data
    python display_digit_table.py

    Display a table of digits from the training data, and click to see more
    python display_digit_table_click.py

    Guess the digit for an 8x8 jpeg image
    python image_to_prediction.py


# Try your own drawn digit

- Visit https://sketch.io/sketchpad/ draw a digit, I used paintbrush with a large brush
- Crop it to a square, and download it
- Resize it in finder to 8x8
- Move it into the right folder 
- Run convert_image.py file with your image
- Copy the resulting array into predict_drawn_digit.py
- Run predict_drawn_digit.py

## Scikit information

Helpful links

Installing scikit-learn
https://scikit-learn.org/stable/install.html

Recognition example:
https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py

Single digit:
https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html

Load digits reference:
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

Other information

To install file to convert image to grayscale matrix:

    pip install opencv-python


### Debugging info

Use of matplotlib in virtualenv on macos
https://markhneedham.com/blog/2018/05/04/python-runtime-error-osx-matplotlib-not-installed-as-framework-mac/
