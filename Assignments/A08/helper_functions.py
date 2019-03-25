import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
import sys
import json
import requests
from math import sqrt
import glob
from PIL import Image,ImageDraw


def brightness(r,g,b):
    """A function to return the calculated "brightness" of a color.
    http://www.nbdtech.com/Blog/archive/2008/04/27/Calculating-the-Perceived-Brightness-of-a-Color.aspx
    Arguments:
        r: int
        g: int
        b: int
    Returns:
        Values between 0-1 (percent of 0-255)
    """
    return sqrt(pow(r,2) * .241  + pow(g,2) * .691 + pow(b,2) * .068 ) / 255
    
def find_histogram(clt):
    """ Create a histogram with k clusters
    Arguments:
        :param: clt
        :return:hist
    Used By:
        get_dominant_colors
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
    

def color_diff(c1,c2):
"""Returns a percent distant from two rgb colors
Params:
    c1 [tuple]: rgb color tuple 
    c2 [tuple]: rgb color tuple 
Returns:
    percent [float]: value between 0 and 1

"""
    d = sqrt(pow((c2[0]-c1[0]),2)+pow((c2[1]-c1[1]),2)+pow((c2[2]-c1[2]),2))

    return d / sqrt(pow(255,2)+pow(255,2)+pow(255,2))
