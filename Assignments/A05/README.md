## Ascii Art - Twist on the classic
#### Due: March 6<sup>th</sup> by classtime.


### Overview

One version of `Ascii Art` is the conversion of photographs or images into a "plain text" representation using simple ascii characters. 

|            |             |
|:----------:|:-----------:|
| <img src="vans-logo.png" width="200"> | <img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/vans.png" width="200"> |

Here is a simple program to do just that can be found [HERE](./ascii_art.py). 

Notice the skew in aspect ratio. This is because ascii characters are printed on lines with added space. We can fix that by reducing the number of lines we output, but not in this assignment. This assignment we are going to create ascii art "images", not just plain text representations of images.



https://www.compart.com/en/unicode/

```python
txtImg = Image.new('RGBA', size, (255,255,255,255))

# get a font
fnt = ImageFont.truetype(self.font_name, self.font_size)

# get a drawing context
d = ImageDraw.Draw(txtImg)

# add a character to some xy 
d.text((x,y), c, font=fnt, fill=(255,0,0))


# Display the image
txtImg.show()

# Save the image (must be a jpg image).
txtImg.save('output.jpg')
```
