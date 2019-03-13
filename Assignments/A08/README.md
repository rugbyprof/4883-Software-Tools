# Photographic mosaic

What is an photgraphic mosaic? 

From Wikipedia:

>In the field of photographic imaging, a photographic mosaic, also known under the term Photomosaic, a portmanteau of photo and mosaic, is a picture (usually a photograph) that has been divided into (usually equal sized) tiled sections, each of which is replaced with another photograph that matches the target photo. When viewed at low magnifications, the individual pixels appear as the primary image, while close examination reveals that the image is in fact made up of many hundreds or thousands of smaller images. Most of the time they are a computer-created type of montage.
>
>There are two kinds of mosaic, depending on how the matching is done. 
>
>**Type 1:**
>
>In the simpler kind, each part of the target image is averaged down to a single color. Each of the library images is also reduced to a single color. Each part of the target image is then replaced with one from the library where these colors are as similar as possible. In effect, the target image is reduced in resolution (by downsampling), and then each of the resulting pixels is replaced with an image whose average color matches that pixel.
>
>**Type 2:**
>
>In the more advanced kind of photographic mosaic, the target image is not downsampled, and the matching is done by comparing each pixel in the rectangle to the corresponding pixel from each library image. The rectangle in the target is then replaced with the library image that minimizes the total difference. This requires much more computation than the simple kind, but the results can be much better since the pixel-by-pixel matching can preserve the resolution of the target image.[[1]]

The 2 types are referring to pure image replacement based on color and or pattern matching. We can see an example of the first type below looking at Abe on the right. But we can also see that the Abe on the left is not simply finding a best "match". The image on the left uses some additional [image editing](https://en.wikipedia.org/wiki/Image_editing) techniques to change the `tint` of a sub-image as well as [alpha compositing](https://en.wikipedia.org/wiki/Alpha_compositing) making each sub-image partially transparent so details of the underlying original image can be seen. 

### Examples 

|  Mosaic with coloring and Transparency      |  Simple Mosaic    |
|:------:|:-------:|
| <img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/abe_lincoln_collage.png" width="300"> | <img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/abe_collage.jpg" width="300"> |


## Solving the Problem

Before we start programming, we need to think about some preliminaries.

1. We need an easy programmatic way of obtaining images by either color or content.
2. We should understand how to read, create, and edit images at the pixel level.
3. We probably also should understand how to quantify colors (averages, distances, counting unique colors, etc.)

### Step 1: Obtaining Sub-Images

If you look at the two examples above, you can see we need **lots** of thumbnails. The left image is about `44*36` or `1584` images. That doesn't mean they are all unique, but that is still a LOT of images. 

There is a nice python library that downloads images in bulk from google. It can be obtained from [here](https://github.com/hardikvasa/google-images-download). The problem is that it downloads full size images AND thumbnails if we want them.  To run the `google-images-download` library, you need to install:

- Install `selenium` 
  - `pip install selenium`
  - Home: https://pypi.org/project/selenium/ 
- Install google_images_download
  - `pip install google_images_download`
  - or download and install: https://github.com/hardikvasa/google-images-download
- Install Chromedriver
  - `pip install chromedriver`
  - Home: http://chromedriver.chromium.org/

I have an altered version of `google-images-download` that just downloads thumbnails. I will make that available on git hub.


### Step 2. Read, Edit, Create images



How I see this happening is this: 

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/Apple_Rainbow.png" width="200">

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/Apple_Rainbow_64.png" width="200">

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/Apple_Rainbow_32.png" width="200">

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/Apple_Rainbow_16.png" width="200">


### Size and Shape

- What is the dominant color in this image?
- It's also not square ... 

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/lilly_400x.jpg" width="400">



#### Editing Images

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/rgb_example.png" width="400">



#### Color

Having the ability to quantify the "dominant" or "average" color of an image is necessary so we can fit a particular small image into a location on the larger image that needs a specific color. To do this, we can use `OpenCV` and `Pillow`. `OpenCV` is a powerful computer vision library, but gives us some functionality that my help us process colors, or more specifically reduce them. `Pillow` is a python library that gives us full control over the creation and editing of images at the pixel and above level. This means I can "paste" images at specific locations, or color pixels as necessary. Here are a couple of links to color reduction and finding the dominant color:

- [Average or Dominant Color](https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv)
- [Kmeans](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html)



### Python Pillow References

- Below are a couple of links to `Pillow` extensive collection of image functions:
  - [effbot.org](http://effbot.org/imagingbook/)
  - [pillow.readthedocs.io](https://pillow.readthedocs.io/en/latest/handbook/tutorial.html)


### Example Approaches

- https://softwareengineering.stackexchange.com/questions/254955/algorithms-for-making-image-mosaics-is-there-a-quicker-way-than-this
- https://williamedwardscoder.tumblr.com/post/84505278488/making-image-mosaics


### Approach As Discussed In Class

- Determine a `chunk` size: `N`. `N=16` is a good place to start. Any smaller and sub images will stop being very identifiable.
- The divide original image into chunks, where each chunk is some `NxN` subsection of original. 
- Process each `chunk` and determine the `dominant` colors.
- Compare 1 or more of those `dominant` colors to your folder of possible `subimages`.
  - The color values for your `subimages` should be pre processed so you only have a 1 time cost.
- Replace the current `chunk` with the closest matching `subimage`

**Thoughts**

- Should shape matter? I think it could improve overall result if shape is accounted for.
- How will you handle object edges? This only matters in images with a transparent background.
- Should you rotate `subimages` to better match original?

### References

[1]: https://en.wikipedia.org/wiki/Photographic_mosaic




