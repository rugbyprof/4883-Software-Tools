"""

"""

import json
from  rich import print 

def processJson():
    with open('dwarf_family_tree.json') as f:
        data = json.load(f)
        

    for person in data:
        print(person)


def processCsv():
    with open('dwarf_family_tree.csv') as f:
        data = f.readlines()
        for line in data:
            print(line.strip().split(','))
            
            
if __name__ == "__main__":
    processJson()
    processCsv()