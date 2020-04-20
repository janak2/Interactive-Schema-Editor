from Code.src.config import *
from Code.src.line_detector import *
from Code.src.main import *

img = load_image("../data/Breaker Schematic Marked.png")
show_image(img)

cd = LineDetector()
red_img = cd.get_color(img)
show_image(red_img)

gray_img = cd.convert_gray_scale(red_img)
show_image(gray_img)

blurred_img = cd.apply_smoothing(gray_img)
show_image(blurred_img)

edge_img = cd.detect_edges(blurred_img)
show_image(edge_img)

list_of_lines = cd.hough_lines(edge_img)
line_image = []
for lines in list_of_lines:
    line_image.append(cd.draw_lines(img, lines))
show_image(line_image)