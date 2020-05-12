# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:41:29 2020

@author: daddyj
"""


import cv2
from config import *
from main import *
from detector import *
import math
import numpy as np

def find_bounding_rect(img):
    h,w = img.shape
    x1,x2,y1,y2 = 0,0,0,0
    for i in range(h):
        empty = True
        for j in range(w):
            empty = empty and img[i,j] == 0
            
        if empty:
            x1 = i
            
def calculate_MHD(stroke, template):
    w,h = template.shape
    s = cd.invert_color(stroke)
    #show_image(s)
    
    template_inv = cd.invert_color(template)
    
    
    locations_s = cv2.findNonZero(s)
    #print(locations_s)
    
    locations_t = cv2.findNonZero(template_inv)
    #print(locations_t)
    
    
    s_x = np.array([x[0][0] for x in locations_s])
    s_y = np.array([x[0][1] for x in locations_s])
    t_x = np.array([x[0][0] for x in locations_t])
    t_y = np.array([x[0][1] for x in locations_t])
    
    ha = 0 
    for temp in locations_s:
        mind = math.inf
        xa = temp[0][0]
        ya = temp[0][1]
        
        d = np.sqrt(np.square(t_x-xa)+np.square(t_y-ya))
        mind = np.amin(d)
        #print(mind)
        ha += mind
    
    print(ha)
    ha *= 1/(len(s_x)**2)

    hb = 0 
    for temp in locations_t:
        mind = math.inf
        xa = temp[0][0]
        ya = temp[0][1]
        
        d = np.sqrt(np.square(s_x-xa)+np.square(s_y-ya))
        mind = np.amin(d)
        #print(d,mind)
        hb += mind
    hb *= 1/(len(t_x)**2)
    mhd = max(ha,hb)
    
    print(ha,hb,len(s_x),len(t_x))
    return mhd

def calculate_MHD_abs(stroke, template):
    w,h = template.shape
    s = cd.invert_color(stroke)
    #show_image(s)
    
    template_inv = cd.invert_color(template)
    
    
    locations_s = cv2.findNonZero(s)
    #print(locations_s)
    
    locations_t = cv2.findNonZero(template_inv)
    #print(locations_t)
    
    
    s_x = np.array([x[0][0] for x in locations_s])
    s_y = np.array([x[0][1] for x in locations_s])
    t_x = np.array([x[0][0] for x in locations_t])
    t_y = np.array([x[0][1] for x in locations_t])
    
    ha = 0 
    for temp in locations_s:
        mind = math.inf
        xa = temp[0][0]
        ya = temp[0][1]
        
        d = 0.5*(np.abs(t_x-xa)+np.abs(t_y-ya))
        mind = np.amin(d)
        #print(mind)
        ha += mind
    
    print(ha)
    ha *= 1/(len(s_x)**2)

    hb = 0 
    for temp in locations_t:
        mind = math.inf
        xa = temp[0][0]
        ya = temp[0][1]
        
        d = 0.5*(np.abs(s_x-xa)+np.abs(s_y-ya))
        mind = np.amin(d)
        #print(d,mind)
        hb += mind
    hb *= 1/(len(t_x)**2)
    mhd = max(ha,hb)
    
    print(ha,hb,len(s_x),len(t_x))
    return mhd

def calculate_MHD_and(stroke, template):
    w,h = template.shape
    s = cd.invert_color(stroke)
    #show_image(s)
    template_inv = cd.invert_color(template)
    
    a = cv2.bitwise_and(s,template_inv)
    show_image(a)
    locations_t = cv2.findNonZero(template_inv)
    
    t = np.sum(a)/(255*len(locations_t))
    
    return t


if __name__ == "__main__":
    cd = Color()
    marked_img = load_image("../data/capacitor_hand.png")
    #marked_img = load_image("../data/line_hand.png")
    mask_green = cd.get_mask(marked_img, GREEN, COLOR_THRESHOLD['GREEN'], "BRG")
    marked_img_nogreen = cd.convert_color(marked_img, mask_green, 1)
    hsv_img = cd.convert_hsv(marked_img_nogreen)
    mask_red = cd.get_mask(hsv_img, RED, COLOR_THRESHOLD['RED'], "HSV")
    marked_img_nored_b = cd.convert_color(marked_img_nogreen, mask_red, 0)
    marked_img_nored_w = cd.convert_color(marked_img_nogreen, mask_red, 1)
    gray = cd.invert_color(mask_red)
    show_image(gray)
    
    #img = cv2.cvtColor(mask_red_invert, cv2.COLOR_RGB2GRAY)
    #show_image(img)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(len(contours))
    
    #find_bounding_rect(mask_red_invert)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
    
        print(x,y,w,h)
        cropped = gray[y:y + h, x:x + w]
        show_image(cropped)
        print(cropped.shape)
        
        cap = load_image("../data/capacitor.png")
        cap = cv2.cvtColor(cap, cv2.COLOR_RGB2GRAY)
        #show_image(cap)
        cap = cv2.resize(cap, (w,h),interpolation =cv2.INTER_AREA)
        show_image(cap)
        print(cap.shape)
        print(calculate_MHD_and(cropped,cap))
        
        
        show_image(gray)
        gray[y:y + h, x:x + w] = cap
        show_image(gray)
    
    
    
    

