""" This module is used to fix the dwarf data from the csv file to be more realistic
    and to add more data to the file.
"""

import csv
from rich import print 
import json 

from helpModule import * 
import random 

ageChoices = genAgeChoices(True)
months = [x for x in range(1,13)]
days = [x for x in range(1,29)]

class Names:
    def __init__(self):
        self.firstNames = []
        self.lastNames = []
        self.clanNames = []
        first_files = ['./names/asian_first_names.csv','./names/dnd_first_names.csv','./names/mock_names.csv']
        last_files = ['./names/asian_surnames.txt','./names/dnd_last_names.txt']
        
        
        for firstFile in first_files:
            with open(firstFile, newline='\n') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.firstNames.append((row['first_name'],row['gender']))
                    if firstFile == './names/mock_names.csv':
                        self.lastNames.append(row['last_name'])

        for lastFile in last_files:
            with open(lastFile) as f:
                rows = f.readlines()
                for row in rows:
                    self.lastNames.append(row.strip().capitalize())
                    
                    
        with open("./names/clan_names.txt") as f:
            rows = f.readlines()
            for row in rows:
                self.clanNames.append(row.strip().capitalize())             

        self.lastNames = list(set(self.lastNames))
        self.firstNames = list(set(self.firstNames))
        self.firstNames = sorted(self.firstNames)
        self.lastNames = sorted(self.lastNames)
        
    def getRandLast(self):
        """get a random last name from the list of last names

        Returns:
            string: a random last name
        """
        return random.choice(self.lastNames)
    
    def getRandFirstPlusGender(self):
        """get a random first name from the list of first names

        Returns:
            string: a random first name
        """
        return random.choice(self.firstNames)
    

    
    def getRandClan(self,id=None):
        """get a random clan name from the list of clan names

        Returns:
            string: a random clan name
        """
        if id:
            self.clanNames = sorted(self.clanNames)
            return self.clanNames[id]
        return random.choice(self.clanNames)
    
nameHelper = Names()

def firstGenderLastClan(clanId=None):
    global nameHelper
    first,gender = nameHelper.getRandFirstPlusGender()
    
    return first,gender,nameHelper.getRandLast(),nameHelper.getRandClan(clanId)

def getBirthDeath(year):
    global ageChoices
    global months
    global days

    # gets an appropriate age for the person (hopefully)
    randAge = getAge(ageChoices)
    birthYear =  int(year) 
    deathYear = birthYear + randAge
    
    month, day = random.choice(months), random.choice(days)
    #print(f"{month}/{day}/{birthYear}")
    birthDate = f"{month}/{day}/{birthYear}"
    
    month, day = random.choice(months), random.choice(days)
    #print(f"{month}/{day}/{birthYear}")
    deathDate = f"{month}/{day}/{deathYear}"


    return birthDate, deathDate, randAge
    
    
def fix_data():
    """ 
    csv columns for dwarf data
        pid, name, gender, generation, byear, dyear, dage, myear, mage, ptype, clan, spouseId, parentId1, parentId2, parentNodeId
    example rows
        0,smith,M,0,1701,1771,70,1719,18,ESTP,5,,,,-1
        146,Flini,M,4,1918,2092,174,1961,43,ENTJ,0,145,,,145
        147,Grini,M,5,1962,2178,216,,,ISTP,0,,145,146,146
        148,Dís,F,5,1973,2296,323,2015,42,ISTJ,3,,145,146,146
    
    OVERVIEW:
        - Replaces the name with a random name from the one of the existing files as well as give a first and last name
        - Adjusts the age to be closer to a human age
        - Replaces clan id with a clan name
        - Renames colums to be more descriptive
        - Saves new data to a json file
    """
    oldData = []
    newData = []
    with open('dwarf_family_tree.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            oldData.append(row)
            birthDate,deathDate,age = getBirthDeath(row['byear'])
            fname,gender,lname,clan = firstGenderLastClan(int(row['clan']))
            newRow = {
                "fname": fname,
                "lname": lname,
                "gender": gender,
                "birthDate": birthDate,
                "deathDate": deathDate,
                "age": age,
                "marriedYear": row['myear'],
                "marriedAge": row['mage'],
                "personality":row['ptype'], 
                "clanName":clan, 
                "spouseId":row['spouseId'], 
                "fatherId":row['parentId1'], 
                "motherId":row['parentId2'], 
                "parentNodeId":row['parentNodeId']
            }
            print(newRow)
            newData.append(newRow)
    return newData

def writeJson(data):
    with open('dwarf_family_tree.json', 'w') as f:
        json.dump(data, f, indent=4)
        
def writeCsv(data):
    with open('dwarf_family_tree2.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
            
if __name__ == "__main__":
    n = Names()
    print(n.getRandFirstPlusGender())
    print(n.getRandLast())
    print(n.getRandClan())
    print(firstGenderLastClan())
    print(firstGenderLastClan())
    print(getBirthDeath(1701))
    print(getBirthDeath(1701))
    newData = fix_data()
    print(newData)
    writeJson(newData)
    writeCsv(newData)