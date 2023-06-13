from rich import print
import random


"""
Simple overview of lists
Lists are mutable (can be changed)
"""
if __name__ == '__main__':
  # create a list
  L1 = [1,2,3,4,5,6,7,'bananas',[9.1,10.3]]
  
  # iterate over the list
  for item in L1:
    # print the item
    print(item)
  
  
  # create a staggered list (almost 2d array list of lists)
  L2 = [[1,2,3],[6,7,8],[88,99,77,101,777]]

  # print the list
  print(L2)

  # print the list in a more readable way  
  for row in L2:
    for item in row:
      print(item,end=" ")
    print()
