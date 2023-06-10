"""

"""

import json
from  rich import print 

with open('dwarf_family_tree.json') as f:
    data = json.load(f)
    

for person in data:
    print(person)


