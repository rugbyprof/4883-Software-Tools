from rich import print
import random


"""
Simple overview of tuples
Tuples are immutable lists (cannot be changed)
"""
if __name__ == '__main__':
    threeD = (1,2,3)
    print(threeD)
    
    # threeD[0] = 5 # This will not work
    
    print(threeD[0]) # This prints 1
    # we can access the elements of a tuple, but not change them


    xy = (random.randint(1,99),random.randint(1,99))

    print(xy)

    x,y = xy    # This is called unpacking and is very useful

    print(x,"---",y)
