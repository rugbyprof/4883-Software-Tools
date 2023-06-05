#!/usr/local/bin/python3

def grab_thumbnails(**kwargs):
    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = kwargs   #creating list of arguments
    paths = response.download(arguments)    #passing the arguments to the function