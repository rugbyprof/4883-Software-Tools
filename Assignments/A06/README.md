## Emoji Scraper - Emojis for image Mosaic
#### Due: Monday 11<sup>th</sup> of March at class time.


### Overview

There are 878 emoji images on the following site: https://www.webfx.com/tools/emoji-cheat-sheet/ . I think we may use them for part of our image mosaic assignment. Use python beautiful soup to scrape all images into a local folder on your machine. Its barely 20 lines of code to get it done. Here is the code that will find the image src's for you:


```python

url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'

# Use beatiful soup to read the page
# then loop through the page with the following


for emoji in page.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']
    print(url+image_path)
    # save the image using requests library
```


### Deliverables

- Create a folder in your assignments folder called `A06`.
- Create a file called `emojigrabber.py` in your `A06` folder.
- Save your emojis in a folder called `emojis`.
- Make sure you zip it before you commit to github.
- Create a `README.md` that describes your project and each file.
- Comment your code with a program comment block and comment any functions you create.
