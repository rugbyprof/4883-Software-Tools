"""
Json methods:
  - load = loads a file into a python dict or list object
  - loads = loads a string into a python dict or list object
  - dump = converts a python list or dict into a string then writes to a file
  - dumps = converts a python list or dict into a string then returns the string
"""
import json
from rich import print
import random

def dictExampleCode():
  """Example code for using a dictionary
  """
  # create a dictionary using our family tree data
  person =  {
      "id": "0",
      "generation": "0",
      "fname": "Gustavus",
      "lname": "Banfill",
      "gender": "M",
      "birthDate": "7/21/1701",
      "deathDate": "2/9/1767",
      "age": 66,
      "marriedYear": "1719",
      "marriedAge": "18",
      "personality": "ESTP",
      "clanName": "Blacksteel",
      "spouseId": "",
      "fatherId": "",
      "motherId": "",
      "parentNodeId": "-1"
  }
  
  # print the dictionary keys
  # could also us person.keys() to get the keys
  for k in person:
    print(k)
    
  # another way to print the dictionary keys
  keys = person.keys()
  print(keys)
    
  # print the dictionary values (not the keys)
  # keys are default, but values need the .values() method
  for v in person.values():
    print(v)
    
  # another way to print the dictionary values
  vals = person.values()
  print(vals)

  # print the dictionary key/value pairs together 
  # .items() returns a list of tuples that get unpacked into k,v
  for k,v in person.items():
    print(k,"=",v)



def createOrgFile():
  """Create a json file with a list of dictionaries
  """
  with open("dwarf_family_tree.json") as f:
    # another way to read a json file
    # data = json.loads(f.read())
    
    data = json.load(f)
  clanDict = {}

  # create a dictionary of clan names and a list of people in that clan
  for p in data:
    # if clan name is not in the dictionary, add it
    if not p['clanName'] in clanDict:
      clanDict[p['clanName']]= []
      
    # add the person to the clan list
    clanDict[p['clanName']].append(p)

  # print the clan names and the number of people in each clan
  for clan,clanList in clanDict.items():
    print(f"{clan}: size:{len(clanList)}")
    
  # return the dictionary
  return clanDict

# only runs if this file is the main file
if __name__ == '__main__':
  dictExampleCode()
  createOrgFile()






