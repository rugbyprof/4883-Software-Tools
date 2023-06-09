"""

"""
import csv
import time
import datetime
import random
import sys

# from module import randomDate
# from module import getAge
# from module import toTimeStamp
# from module import secondsToYears
# from module import genNumChildChoices
# from module import genAgeChoices
# from module import howManyKids

# this line replaces all the individual imports from above
from helpModule import *

# seed the random number generator with system time to 
# get different results each time
random.seed(datetime.datetime.now().timestamp())


# list of numbers from 1 to 5 weighted to return more 1s than 5s essentially
numkids = genNumChildChoices()

# list of ages weighted to return more 70+ and 80+ ages than 1-5 ages
ages = genAgeChoices()


print(getAge(ages))

print(randomDate("1780", "2009"))

print(numkids)

print(howManyKids(numkids))
date_format = '%Y-%m-%d'



# with open('family_tree_seed_data.csv', newline='\n') as csvfile:
#   reader = csv.DictReader(csvfile)
#   for row in reader:
#     print(row['first_name'], row['last_name'], row['birth_date'],
#           row['death_date'])

#     birthYear = row['birth_date'][-4:]
#     deathYear = row['death_date'][-4:]
#     print(birthYear, deathYear)

"""
- generate a person 
  - Name
  - DOB  
  - DOD   
  - AGE 
- Marry two people
- determine how many children they have
- process each child and decide to marry them
"""