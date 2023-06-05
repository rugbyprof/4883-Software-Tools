def int_to_ascii(val):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """
    if not isinstance(val, int):
        raise TypeError("val is not int")
    
    if not val >= 0 and val <= 255:
        raise ValueError("val is not 0-255")

    ascii_chars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']

    return ascii_chars[val//25]

if __name__=='__main__':
    try:
        int_to_ascii(-1)
    except:
        print("val is not 0-255")
    
    try:
        int_to_ascii("A")
    except:
        print("val is not int")

    print(int_to_ascii(100))
