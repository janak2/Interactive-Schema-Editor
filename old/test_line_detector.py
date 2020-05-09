<<<<<<< Updated upstream:src/test_line_detector.py
from Code.src.config import *
from Code.src.line_detector import *
from Code.src.main import *
=======
from line_detector import *
from main import *
from config import *
from color_detector import *
from text_detector import *
>>>>>>> Stashed changes:old/test_line_detector.py

img = load_image("../data/Breaker Schematic Marked.png")
show_image(img)

cd = LineDetector()
red_img = cd.get_color(img)
show_image(red_img)

gray_img = cd.convert_gray_scale(red_img)
show_image(gray_img)

blurred_img = cd.apply_smoothing(gray_img)
show_image(blurred_img)

<<<<<<< Updated upstream:src/test_line_detector.py
edge_img = cd.detect_edges(blurred_img)
show_image(edge_img)

list_of_lines = cd.hough_lines(edge_img)
line_image = []
for lines in list_of_lines:
    line_image.append(cd.draw_lines(img, lines))
show_image(line_image)
=======
# Create red mask from marked image
hsv_img = LineDetector().convert_hsv(new_img)
#show_image(hsv_img)
red_mask, masked_img = LineDetector().get_color(hsv_img)
#show_image(masked_img)

red_mask_invert = LineDetector().invert_color(red_mask)
#show_image(red_mask_invert)

# Remove All Green from marked image
blank, mask = ColorDetector().get_color_image(new_img, RED, COLOR_THRESHOLD['RED'])
show_image(blank)

# Create text from image
text_img = TextDetector().get_text(red_mask_invert, new_img)
show_image(text_img)

# convert all red into black on marked image and show new image
new_img = LineDetector().convert_color(new_img, red_mask, blank)
show_image(new_img)

# hls_img = cd.convert_hls(img)
# show_image(hls_img)

# gray_img = LineDetector().convert_gray_scale(masked_img)
# show_image(gray_img)

# blurred_img = cd.apply_smoothing(gray_img)
# show_image(blurred_img)

# edge_img = cd.detect_edges(gray_img)
# show_image(edge_img)

# red_img, mask = ColorDetector().get_color_image(img, RED, COLOR_THRESHOLD['RED'])
# show_image(red_img,"red")

# list_of_lines = cd.hough_lines(edge_img)
# line_img = red_img
# for lines in list_of_lines:
#    line_img = cd.draw_lines(line_img, lines)
# show_image(line_img)
>>>>>>> Stashed changes:old/test_line_detector.py
