from line_detector import *
from main import *
from config import *
from color_detector import *

# Load all images
test_image_list = load_image_list()

# Select which image to analyse
# ---- Select 1 for Breaker Schematic Diagram
# ---- Select 2 for One Line Diagram
image_select = 1

# show original and marked image
original_img = test_image_list[2 * image_select - 2]
show_image(original_img)
marked_img = test_image_list[2 * image_select - 1]
show_image(marked_img)

# Remove All Green from marked image
new_img, mask = ColorDetector().get_color_image(marked_img, GREEN, COLOR_THRESHOLD['GREEN'])
show_image(new_img)

# Create red mask from marked image
hsv_img = LineDetector().convert_hsv(new_img)
show_image(hsv_img)
red_mask, masked_img = LineDetector().get_color(hsv_img)
show_image(masked_img)

# convert all red into black on marked image and show new image
new_img = LineDetector().convert_color(new_img, red_mask)
show_image(new_img)



# hls_img = cd.convert_hls(img)
# show_image(hls_img)

# gray_img = cd.convert_gray_scale(red_img)
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
