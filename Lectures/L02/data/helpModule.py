import random
import time
import datetime


def genAgeChoices(oldOnly=False):
  """Creates a list of age choices based on a weighted averages. Meaning more 
     70+ and 80+ ages will be returned than 
  """
  ages = []
  # Define the age ranges and their corresponding weights
  # probably not totally accurate when compared to real life
  ageRanges = [(50, 59, 5), (60, 69, 9), (70, 79, 20),
               (80, 89, 32), (90, 99, 23), (100, 109, 5)]
  if not oldOnly:
    ageRanges += [(1, 5, 1), (20, 49, 5)]
    
  for ageTuple in ageRanges:
    for i in range(ageTuple[2]):
      ages.append(random.randint(ageTuple[0], ageTuple[1] + 1))

  random.shuffle(ages)

  return ages


def genNumChildChoices():
  """
  Families with one child: Approximately 20-25%.
  Families with two children: Approximately 35-40%.
  Families with three children: Approximately 20-25%.
  Families with four children: Approximately 10-15%.
  Families with five children: Approximately 5-10%.
  """
  numkids = []
  numkids += [1 for x in range(22)]
  numkids += [2 for x in range(37)]
  numkids += [3 for x in range(22)]
  numkids += [4 for x in range(12)]
  numkids += [5 for x in range(7)]

  return numkids

"""
https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
"""


def randomDate(start, end, time_format='%m/%d/%Y',specific = False):
  """Get a random date between start and end
  Params:
    start: start date
    end: end date 
    time_format: format of the date
    specific: if True, then the date will be a specific date in the range within same year
  Usage:
    randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", '%m/%d/%Y %I:%M %p')
    randomDate("1/1/2008", "1/1/2009", '%m/%d/%Y')
    randomDate(2008, 2009,'%m/%d/%Y',True)
    
  """

  if isinstance(start, int) or (isinstance(start, str) and len(start) == 4):
    start = str(f"01/01/{start}")

  if isinstance(end, int) or (isinstance(end, str) and len(end) == 4):
    end = str(f"01/01/{end}")

  stime = time.mktime(time.strptime(start, time_format))
  etime = time.mktime(time.strptime(end, time_format))

  if not specific:
    ptime = stime + random.random() * (etime - stime)
  else:
    # specChoices = [0.25,0.5,0.75]
    specChoices = [x for x in range(-0.1,0.9)]
    ptime = stime + random.choice(specChoices) * (etime - stime)

  return time.strftime(time_format, time.localtime(ptime))



def getAge(ages):
  """randomly choose a persons age from the weighted ages list
  Params:
    ages: list of ages to choose from
  Returns: 
    age: a random age from the list
  """
  random.shuffle(ages)
  return ages[0]

def toTimeStamp(s):
  """string date into a timestamp
  Params:
    s: string date
  Returns:
    ts: timestamp
  """
  ts = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
  return ts


def secondsToYears(d):
  """Takes an integer of seconds and converts it to years

  Args:
      d (int): seconds

  Returns:
      _type_: _description_
  """
  years = d / 3600 / 24 / 365
  return int(years)

def generatePerson(startYear):
  """Create a persons bday and death day given a start year
  """
  pass


def howManyKids(kids):
  """ How many kids should a married couple have.
  """
  random.shuffle(kids)
  return kids[0]

