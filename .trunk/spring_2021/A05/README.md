## Ascii Art - Twist on the classic
#### Due: Wednesday, March 6<sup>th</sup> by classtime.


### Overview

One version of `Ascii Art` is the conversion of photographs or images into a "plain text" representation using simple ascii characters. 

|            |             |
|:----------:|:-----------:|
| <img src="vans-logo.png" width="200"> | <img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/vans.png" width="200"> |

Here is a simple program to do just that can be found [HERE](./ascii_art.py). 

Notice the skew in aspect ratio. This is because ascii characters are printed on lines with added space. We can fix that by reducing the number of lines we output, but not in this assignment. This assignment we are going to create ascii art "images", not just plain text representations of images.

### Steps

- Find a font, possibly from https://www.dafont.com/. I will work on printing unicode emoji's onto Pil images.

```python
 ascii_chars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
```
- Replace the characters from above, with your own set of characters from your new font.
- Process your image one pixel at a time converting each pixel to some appropriate character from your new list. The method typically used for a grayscale image is to find the "average" of each color channel, and use that single value as a lookup index from your array of possible characters:

```python
r,g,b = (123,200,14)
gray = int((r + b + g) / 3)
char = ascii_chars[gray // 25]
```
How you do your character lookup is up to you. If you find a method to match a character to a color without grayscaling first, then awesome! But, the main goal is to write your new "character" to the new image at the proper location and as the proper color.

### Text to Image

Below is an example of writing a letter (of a specific font) to a new drawable image:

```python
# Open a new image using 'RGBA' (a colored image with alpha channel for transparency)
#              color_type      (w,h)     (r,g,b,a) 
#                   \           /            /
#                    \         /            /
newImg = Image.new('RGBA', size, (255,255,255,255))

# Open a TTF file and specify the font size
fnt = ImageFont.truetype('yourfont.ttf', 12)

# get a drawing context for your new image
drawOnMe = ImageDraw.Draw(newImg)


## You would loop through your old image and write on the newImg with the 
## lines of code below:

# add a character to some xy 
#         location   character  ttf-font   color-tuple
#            \         /        /            /
#             \       /        /            /
drawOnMe.text((x,y), c, font=fnt, fill=color)

# Display your new image with all the stuff `drawOnMe` placed on it
newImg.show()

# Save the image.
newImg.save('output.jpg')
```

### Deliverables

- Create a folder called `A05` in your assignments folder.
- Place all your code in a file called `ascii_image.py`
- Use functions when appropriate.
- Comment using a code block at the top of your file and for each function.
- Input images should be read from a folder called `input_images` 
- Output images should be written to a folder called `output_images`
- Output images should be made up of colored text using your new characters. 
- Spacing of characters should be adjusted so that the image looks recognizable from the original. Some overlap of characters is acceptable and even encouraged if it makes the picture look good.
- **Important**
    - A user should be able to run your program from the command line and provide the following information:
        - Input file (image to process)
        - Output file name (path and name of where to save it)
        - True type font (a path and name to a true type font)
        - Font size (integer of what font size they want)
    - Python sends command line arguments to your program as a list that is named `sys.argv`. 
    - You must `import sys` to use `sys.argv`
    
    
