from main import *
from config import *
from detector import *

# load and display original and marked image
original_img = load_image("../data/Breaker Schematic.png")
show_image(original_img)
marked_img = load_image("../data/Breaker Schematic Marked.png")
show_image(marked_img)

# load and display original and marked image
#original_img = load_image("../data/One Line.png")
#show_image(original_img)
#marked_img = load_image("../data/One Line Marked.png")
#show_image(marked_img)

cd = Color()

# Remove ALL Green from marked image
mask_green = cd.get_mask(marked_img, GREEN, COLOR_THRESHOLD['GREEN'], "BRG")
#show_image(mask_green)

marked_img_nogreen = cd.convert_color(marked_img, mask_green, 1)
show_image(marked_img_nogreen)


# Add ALL Red from marked image
hsv_img = cd.convert_hsv(marked_img_nogreen)
mask_red = cd.get_mask(hsv_img, RED, COLOR_THRESHOLD['RED'], "HSV")
#show_image(mask_red)

marked_img_nored_b = cd.convert_color(marked_img_nogreen, mask_red, 0)
#show_image(marked_img_nored_b)

marked_img_nored_w = cd.convert_color(marked_img_nogreen, mask_red, 1)
#show_image(marked_img_nored_w)


#Identify and add red text
mask_red_invert = cd.invert_color(mask_red)
#show_image(mask_red_invert)


# Create text from image
cd = Text()
marked_img_text = cd.get_text(mask_red_invert, marked_img_nogreen, marked_img_nored_w)
show_image(marked_img_text)

# convert all red into black on marked image and show new image
#new_img = LineDetector().convert_color(new_img, red_mask, blank)
#show_image(new_img)


