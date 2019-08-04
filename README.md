# Digit recognition demo

Download files.

    mkvirtualenv digits
    pip install -r reqs.txt

========

pip install scikit-learn
pip install matplotlib

To return:
workon digits

python display_digit.py
python display_digit_table.py
python display_digit_table_click.py


# Try your own drawn digit

- Visit https://sketch.io/sketchpad/ draw a digit, I used paintbrush with a large brush
- Crop it to a square, and download it
- Resize it in finder to 8x8
- Move it into the right folder 
- Run convert_image.py file with your image
- Copy the resulting array into predict_drawn_digit.py
- Run predict_drawn_digit.py


Other information

To install file to convert image to grayscale matrix:

    pip install opencv-python
