# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:33:58 2021

@author: HAMEEM
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from PIL import Image
import cv2
cap = cv2.VideoCapture('bird.mp4')
frame_count = 0
crop_start_x = 0
crop_end_x = 12000
crop_start_y = 0
crop_end_y = 12000
frame_skip = 3
#grid
x_grid = 4
y_grid =  8
a4_width, a4_height = A4
pages = x_grid * y_grid
flip_page_width = int( a4_width / x_grid )
flip_page_height = int( a4_height / y_grid )
print("page_width=", flip_page_width)

while(cap.isOpened()):
    if frame_skip > 1:
        for i in range(frame_skip):
            ret, frame = cap.read()
    else:
        ret, frame = cap.read()
    

    gray_orig = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    im_shape = gray_orig.shape
    
    if crop_start_y > im_shape[0]:
        crop_start_y = 0
    if crop_end_y > im_shape[0]:
        crop_end_y = im_shape[0]
    if crop_start_x > im_shape[1]:
        crop_start_x = 0
    if crop_end_x > im_shape[1]:
        crop_end_x = im_shape[1]
    gray_crop = gray_orig[crop_start_y:crop_end_y, crop_start_x:crop_end_x]
    dim = (flip_page_width, flip_page_height)
    gray = cv2.resize(gray_crop, dim, interpolation = cv2.INTER_AREA)

        

    #cv2.imshow('frame',gray)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    file_string = 'images/file_' + str(frame_count) + '.jpg'
    cv2.imwrite(file_string, gray)
    print(file_string)
    frame_count += 1
    if frame_count > pages:
        break
  
total_images = frame_count - 1
pos_x = 0
pos_y = 0
c = canvas.Canvas("flipbook.pdf")
for i in range(total_images):
    file_string = 'images/file_' + str(i) + '.jpg'

    pdf_image = Image.open(file_string)
    #c.drawString(100,750,"Welcome to Reportlab!")
    c.drawInlineImage(pdf_image, pos_x, pos_y, width= flip_page_width, height = flip_page_height )
    c.drawString(pos_x,pos_y,str(i+1))
    print(file_string, pos_x, pos_y)
    c.line(pos_x, pos_y, a4_width, pos_y)
    c.line(pos_x, pos_y, pos_x, a4_height)
    
    if ((i+1) % x_grid) == 0:
        pos_y = int(pos_y + flip_page_height )
        pos_x = 0
    else:
        pos_x = int( pos_x + flip_page_width )

c.save()