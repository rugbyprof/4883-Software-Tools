#!/usr/local/bin/python3
"""
This package has the following function:

get_main_color():
    If receives a path to an image file and returns the main color.
    It will also reduce the number of colors in the image if wanted.

named_color():
    Returns the closest named color from the dictionary below.
    Also returns the dominant channel (r or g or b)

color_summary():
    Summarizes the image colors into a dictionary of helpful 
    values for comparing colors. See function comment.

"""
import glob
import os,sys
import cv2
from PIL import Image
import numpy as np
import pprint
from matplotlib import pyplot as plt
from sklearn.cluster import MiniBatchKMeans

colors_dict = {
    'red':[255,0,0],
    'orange':[255,128,0],
    'yellow':[255,255,0],
    'green':[0,255,0],
    'teal':[0,128,128],
    'blue':[0,0,255],
    'purple':[128,0,128],
    'pink':[255,192,203],
    'white':[255,255,255],
    'gray':[128,128,128],
    'black':[0,0,0],
    'brown':[165,42,42]
}


"""
Function: get_main_color
    Finds the "main" color or dominant color.
Params:
    path        [string]   : path to image  
    reduce      [bool]     : reduce colors or not
    num_colors  [int]      : number of colors to reduce to
Returns:
    summary [dict] : see below
"""

def get_main_color(file,reduce=False,num_colors=8):

    if reduce:
        img = reduce_colors(file,num_colors)
    else:
        img = Image.open(file)

    width,height = im.size

    colors = img.getcolors(width*height) #put a higher value if there are many colors in your image
    
    max_occurence, most_present = 0, 0

    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

"""
Returns the closest named color from dict above.
Also returns the dominant r,g,b 

Examples: 
    (99, 136, 95) returns ('gray', 'g')
    (216, 166, 9) returns ('orange', 'r')

"""
def named_color(color):
    closest_rgb = 99999
    closest_name = None
    highest_rgb = None
    highest_val = 0
    
    for name,rgb in colors_dict.items():
        val = 0
        for i in range(3):
            val += abs(color[i] - rgb[i])
        if val < closest_rgb:
            closest_rgb = val
            closest_name = name
    
    if color[0] > color[1]:
        highest_rgb = 'r'
        highest_val = color[0]
    else:
        highest_rgb = 'g'
        highest_val = color[1]
    
    if color[2] > highest_val:
        highest_rgb = 'b'
        highest_val = color[2]

    return closest_name,highest_rgb

"""
Function: 
    color_summary
Params:
    im [pil image]
Returns:
    summary [dict] : see below
'named_colors': {'counts': {'black': 11057,
                             'brown': 6907,
                             'gray': 19187,
                             'green': 117,
                             'pink': 313,
                             'teal': 12648,
                             'white': 94,
                             'yellow': 2},
                  'ratios': {'black': 0.22,
                             'brown': 0.14,
                             'gray': 0.38,
                             'green': 0.0,
                             'pink': 0.01,
                             'teal': 0.25,
                             'white': 0.0,
                             'yellow': 0.0}},
 'rgb': {'counts': {'b': 415, 'g': 47123, 'r': 2787},
         'ratios': {'b': 0.01, 'g': 0.94, 'r': 0.06}},
 'total_colors': 50325}
"""
def color_summary(im):
    color_count = {
        'rgb':{
            'counts':{},
            'ratios':{}
        },
        'named_colors':{
            'counts':{},
            'ratios':{}
            },
        'total_colors':0
        }
    for c in list(im.getdata()):
        color_count['total_colors'] += 1
        color,rgb = named_color(c)
        if not color in color_count['named_colors']['counts']:
            color_count['named_colors']['counts'][color] = 0
        color_count['named_colors']['counts'][color] += 1

        if not rgb in color_count['rgb']['counts']:
            color_count['rgb']['counts'][rgb] = 0
        color_count['rgb']['counts'][rgb] += 1


    for c,count in color_count['named_colors']['counts'].items():
        color_count['named_colors']['ratios'][c] = round(count / color_count['total_colors'],2)

    for c,count in color_count['rgb']['counts'].items():
        color_count['rgb']['ratios'][c] = round(count / color_count['total_colors'],2)

    return color_count


"""
Function: color_summary
    Returns a pil image with reduced colors using kmeans clustering
    by opencv
Params:
    path        [string]   : path to image  
    numcolors   [int]      : num colors to reduce to
    show        [bool]     : display image in gui
Returns:
    summary [dict] : see below
"""
def reduce_colors(path,numcolors,show=False):

    tmpfile = '/tmp/tmpimage.jpg'

    img = cv2.imread(path)
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = numcolors
    ret,labels,centers=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    res2 = res.reshape((img.shape))

    # save opencv version to tmp dir
    cv2.imwrite(tmpfile,res2)

    if show:
        cv2.imshow('res2',res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return Image.open(tmpfile)

"""
above uses python pil to some extent, this one sticks with opencv
"""
def reduce_colors2(image,K=4):

    if isinstance(image,str):
        if os.path.isfile(image):
            image = cv2.imread(image)
        else:
            print("Error: image arg is string but not valid file.")
            sys.exit()

    if not isinstance(image, np.ndarray):
        print("Error: image arg is not a string but not a valid numpy array either.")
        sys.exit()

    print(K)
    
    (h, w) = image.shape[:2]
    
    # convert the image from the RGB color space to the L*a*b*
    # color space -- since we will be clustering using k-means
    # which is based on the euclidean distance, we'll use the
    # L*a*b* color space where the euclidean distance implies
    # perceptual meaning
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    # reshape the image into a feature vector so that k-means
    # can be applied
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    
    # apply k-means using the specified number of clusters and
    # then create the quantized image based on the predictions
    clt = MiniBatchKMeans(n_clusters = K)
    labels = clt.fit_predict(image)
    quant = clt.cluster_centers_.astype("uint8")[labels]
    
    # reshape the feature vectors to images
    quant = quant.reshape((h, w, 3))
    image = image.reshape((h, w, 3))
    
    # convert from L*a*b* to RGB
    quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

    return quant

def matchShapes(img1,img2):
    image2name = img2
    if isinstance(img1,str):
        if os.path.isfile(img1):
            img1 = cv2.imread(img1,0)
        else:
            print("Error: image arg is string but not valid file.")
            sys.exit()

    if isinstance(img2,str):
        if os.path.isfile(img2):
            img2 = cv2.imread(img2,0)
        else:
            print("Error: image arg is string but not valid file.")
            sys.exit()

    if not isinstance(img1, np.ndarray):
        print("Error: image arg1 is not a string but not a valid numpy array either.")
        sys.exit()

    if not isinstance(img2, np.ndarray):
        print("Error: image arg2 is not a string but not a valid numpy array either.")
        sys.exit()

    ret, thresh = cv2.threshold(img1, 127, 255,0)
    ret2, thresh2 = cv2.threshold(img2, 127, 255,0)
    contours,hierarchy = cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    contours,hierarchy = cv2.findContours(thresh2,2,1)
    if len(contours) == 0:
        return 1000000
    cnt2 = contours[0]

    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    if ret == 1.7976931348623157e+308:
        return 1000000

    return ret

def color_distance(im1,im2,size=(128,128)):

    im1 = cv2.imread(im1)
    im1 = cv2.resize(im1,size)

    im2 = cv2.imread(im2)
    im2 = cv2.resize(im2,size)

    colors = ('b','g','r')

    comparisons = {
        'correlation':cv2.HISTCMP_CORREL,
        'chisquare':cv2.HISTCMP_CHISQR,
        'intersect':cv2.HISTCMP_INTERSECT,
        'bhattacharyya':cv2.HISTCMP_BHATTACHARYYA
    }

    hists = [{},{}]
    
    for i,col in enumerate(colors):
        hists[0][col] = cv2.calcHist([im1],[i],None,[256],[0,256])
    #     plt.plot(hists[0][col],color = col)
    #     plt.xlim([0,256])
    # plt.show()

    for i,col in enumerate(colors):
        hists[1][col] = cv2.calcHist([im2],[i],None,[256],[0,256])
    #     plt.plot(hists[0][col],color = col)
    #     plt.xlim([0,256])
    # plt.show()


    d = {}
    for key,comp in comparisons.items():
        d[key] = {}
        for c in colors:
            d[key][c] = cv2.compareHist(hists[0][c], hists[1][c],comp) 
    pprint.pprint(d)




if __name__=='__main__':
    # im = reduce_colors2("/Users/griffin/Dropbox/Scripts-random/image_projects/downloads/corn-blue/3. mp,550x550,matte,ffffff,t.3u5.jpg",5)
    # cv2.imshow("image", im)
    # cv2.waitKey(0)

    results = {}
    images = {}
    imagesList = glob.glob('/Users/griffin/Dropbox/Scripts-random/image_projects/EmojiColors/emojis_64x64'+'/*.png')

    img1 = '/Users/griffin/Dropbox/Scripts-random/image_projects/EmojiColors/emojis_64x64/lollipop.png'
    for img2 in imagesList:
        results[os.path.basename(img2)] = matchShapes(img1,img2)
        #images[os.path.basename(img2)] = bw
    
    results = sorted([(v, k) for (k, v) in results.items()])
    print(results[:25])

    bw1 = cv2.imread('/Users/griffin/Dropbox/Scripts-random/image_projects/EmojiColors/emojis_64x64/lollipop.png',0)
    ret1, thresh1 = cv2.threshold(bw1, 127, 255,0)
    cv2.imshow('res2',thresh1)
    cv2.waitKey(0)
    
    bw2 = cv2.imread('/Users/griffin/Dropbox/Scripts-random/image_projects/EmojiColors/emojis_64x64/'+results[0][1],0)
    ret2, thresh2 = cv2.threshold(bw2, 127, 255,0)
    cv2.imshow('res2',thresh2)
    cv2.waitKey(0)

    # i = 0
    # for name,val in results.items():
    #     cv2.imshow('img',images[name])
    #     i += 1
    #     if i >= 5:
    #         sys.exit()


    #im = Image.open("./downloads/forest-red/5.jpg")
    # im = Image.open("/Users/griffin/Dropbox/Scripts-random/image_projects/AsciiArt/original_images/lilly_400x.jpg")
    # width,height = im.size
    # print(width,height)
    # histogram = im.histogram()
    # print(histogram)

    # pprint.pprint(color_summary(im))

    # abe1 = '/Users/griffin/Dropbox/Scripts-random/image_projects/image_collage/downloads/forest-red/4.jpg'
    # abe2 = '/Users/griffin/Dropbox/Scripts-random/image_projects/image_collage/downloads/forest-red/5.jpg'
    # abe2 = '/Users/griffin/Dropbox/Scripts-random/image_projects/image_collage/downloads/forest1/4.jpg'
    # abe1 = '/Users/griffin/Dropbox/Scripts-random/image_projects/image_collage/downloads/forest1/4.jpg'

    # color_distance(abe1,abe2)
