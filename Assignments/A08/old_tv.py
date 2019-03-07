#!/usr/local/bin/python3
import sys,os
os.chdir('/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Assignments/A08')

from PIL import Image, ImageDraw
from image_package.color_functions import color_distance
import glob
import random

def tv_pixel(draw,x,y,rgb):

    x *= 3
    y *= 3

    red = (rgb[0],0,0)
    green = (0,rgb[1],0)
    blue = (0,0,rgb[2])

    # draw.line((xy[0]-1, xy[0]-1, xy[0]-1, xy[0]+1), fill = red)
    # draw.line((xy[0]  , xy[0]-1, xy[0],   xy[0]+1), fill = green)
    # draw.line((xy[0]+1 ,xy[0]-1, xy[0]+1, xy[0]+1), fill = blue)

    draw.line((x,  y, x,   y+2), fill = red)
    draw.line((x+1,y, x+1, y+2), fill = green)
    draw.line((x+2,y, x+2, y+2), fill = blue)

    #draw.point((100, 100), 'red')


if __name__=='__main__':
    

    im = Image.open('Apple_Rainbow.png')
    ow,oh = im.size

    nw = ow * 3
    nh = oh * 3

    tvim = Image.new('RGBA', (nw, nh),"white")
    draw = ImageDraw.Draw(tvim)

    data = list(im.getdata())

    print(len(data))

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
        print("%d,%d"%(x,y))
    tvim.show()
    tvim.save('tvout.png')
    #     
    #     #print(pix)
    #     x += 1
    #     i += 1
    #     if x > w:
    #         x = 0
    #         y += 3
    #         i = i - (i%256)
    #         print(i)
    #     #print("%d,%d"%(x,y))
