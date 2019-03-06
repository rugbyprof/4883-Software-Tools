#!/usr/local/bin/python3
import sys
sys.path.append('/Users/griffin/Dropbox/Scripts-random/image_projects/image_package')

from PIL import Image
import google_images_download #importing the library
from image_package.color_functions import color_distance
import glob
import random


"""

"""
def paste2images():
    im = Image.new("RGB", (1024, 1024), "white")

    im1 = Image.open('./Resources/emojis_64x64/-1.png')
    im2 = Image.open('./Resources/emojis_64x64/+.png')

    bbx1 = im1.getbbox()
    bbx2 = im2.getbbox()

    print(bbx1)
    print(bbx2)

    im.paste(im1, (10,10))
    im.paste(im2, (225,0))

    im.show()

def pasteRandomLocations():
    files = glob.glob('./Resources/emojis_64x64/**/*.png', recursive=True)
    print(len(files))
    im = Image.new("RGBA", (1024, 1024), "white")

    for f in files:
        tmp = Image.open(f).convert("RGBA")
        im.paste(tmp, (random.randint(0,1024-64),random.randint(0,1024-64)),tmp)
        tmp.close()
    im.show()

def pasteInOrder():
    files = glob.glob('./Resources/emojis_64x64/**/*.png', recursive=True)

    print(len(files))
    
    im = Image.new("RGBA", (1924, 1924), "white")

    x = 0
    y = 0
    for f in files:
        tmp = Image.open(f).convert("RGBA")
        im.paste(tmp, (x,y),tmp)
        tmp.close()
        x += 64
        if x > 1924:
            x = 0
            y += 64
    im.show()

paste2images()
pasteRandomLocations()
pasteInOrder()
