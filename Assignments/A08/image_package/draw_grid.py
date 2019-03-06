#!/usr/local/bin/python3
import cv2
from PIL import Image, ImageDraw



def thick_line(img,coords,fill,thickness=1,xy='x'):
    x1,y1,x2,y2 = coords

    dx=0
    dy=0
    for i in range(thickness):
        coord = x1+dx,y1+dy,x2+dx,y2+dy
        img.line(coord, fill=fill)
        if 'x' in xy:
            dx += 1
        else:
            dy += 1
    return img



if __name__=='__main__':

    path = "/Users/griffin/Dropbox/Scripts-random/image_projects/AsciiArt/original_images/python_256.png"
    path = "/Users/griffin/Dropbox/Scripts-random/image_projects/AsciiArt/original_images/Apple_Rainbow.png"

    image_name,ext = path.split('.')
    

    im = Image.open(path)

    draw = ImageDraw.Draw(im)

    size = 16

    space = 0
    w,h = im.size
    fill = 255

    while space < w:
        # tuples for line coords
        yline = (space,0,space,h)
        xline = (0,space,w,space)
        
        # draw the lines in the up and down and left and right
        draw = thick_line(draw,yline,(0,0,0),2,'x')
        draw = thick_line(draw,xline,(0,0,0),2,'y')

        # move lines over and down
        space += size

    # draw lines on bottom and far left
    draw = thick_line(draw,(w-2,0,w-2,h),(0,0,0),2,'x')
    draw = thick_line(draw,(0,h-2,w,h-2),(0,0,0),2,'y')
    im.show()


    out_name = image_name+'_'+str(size)+'.'+ext
    print(out_name)
    im.save(out_name, "PNG")
