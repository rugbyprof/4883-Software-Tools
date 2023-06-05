#!/usr/local/bin/python3
import sys,os
os.chdir('/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Assignments/A08')

from PIL import Image, ImageDraw
from image_package.color_functions import color_distance
import glob
import random

"""
Draws an old timey tv image pixel using three vertical bars: r g b
                                                             r g b
                                                             r g b
https://retrocomputing.stackexchange.com/questions/2215/square-pixels-and-tv-output
                                                        
"""
def tv_pixel(draw,x,y,rgb):

    # shift xy by 3 times
    x *= 3
    y *= 3

    # make each vert line = to amount of R or G or B
    red = (rgb[0],0,0)
    green = (0,rgb[1],0)
    blue = (0,0,rgb[2])

    # draw the vert lines
    draw.line((x,  y, x,   y+2), fill = red)
    draw.line((x+1,y, x+1, y+2), fill = green)
    draw.line((x+2,y, x+2, y+2), fill = blue)


if __name__=='__main__':
    

    im = Image.open('nvidia.png')
    ow,oh = im.size

    nw = ow * 3
    nh = oh * 3

    tvim = Image.new('RGBA', (nw, nh),"white")
    draw = ImageDraw.Draw(tvim)

    data = list(im.getdata())

    x = 0
    y = 0
    i = 0
    while i < ow*oh:
        tv_pixel(draw,x,y,data[i])
        i += 1
        x += 1
        if x >= ow:
            x = 0
            y += 1
    tvim.show()
    tvim.save('tvout.png')