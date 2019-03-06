## Image Compare - Mean Square Error
#### Due: March 15<sup>th</sup> by Classtime


### Overview

Using the article written here:
- https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/

Write a small program that:
- Given the input name of an image
- Will find the closest match in a specified folder of images
- e.g. : `python3 match.py folder=emoticons image=boom.png`

### Deliverables

- Create a folder in your assignments folder called `A07`.
- Create a file called `match.py` in your `A07` folder.
- Create a `README.md` that describes your project and each file.
- Comment your code with a program comment block and comment any functions you create.
- When your program is done running, its final act will be to show the image and its closest match to the user. The closest match should not be itself.
- There is a library called `argparse` that helps with command line arguments, but for simple programs sometimes I like to use something like the following to get command line keyword args:

```python
import sys
# This assumes arguments are like: key1=val1 key2=val2 (with NO spaces between key equal val!)
args = {}

for arg in sys.argv[1:]:
    k,v = arg.split('=')
    args[k] = v


# now you have a dictionary with your command line args
```


