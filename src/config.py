COLOR_THRESHOLD = {'GREEN': 70, 'RED': 80}

GREEN = (60, 220, 60) #BGR
RED = (80, 100, 250) #BGR
BLUE = (250,60,60) #BGR

def convert_BGR_to_hex(color):
    return '#%02x%02x%02x' % color[::-1]

