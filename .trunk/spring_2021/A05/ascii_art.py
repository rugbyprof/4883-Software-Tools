import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def img_to_ascii(**kwargs):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """
    ascii_chars = [ u'🦍', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
  
    width = kwargs.get('width',200)
    path = kwargs.get('path',None)

    im = Image.open(path)

    im = resize(im,width)

    w,h = im.size

    print(w,h)

    im = im.convert("L") # convert to grayscale

    imlist = list(im.getdata())

    i = 1
    for val in imlist:
        ch = ascii_chars[val // 25].decode('utf-8')
        sys.stdout.write()
        i += 1
        if i % width == 0:
            sys.stdout.write("\n")

    

def resize(img,width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """
    
    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width ,hsize), Image.ANTIALIAS)

    return img


if __name__=='__main__':
    path = 'vans.jpg'
    Ascii = img_to_ascii(path=path,width=150)
