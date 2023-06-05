import json
import sys
import os
import pprint as pp

os.chdir("/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Resources/creepy")


with open("dictionary_clean.json","r") as f:
    data = json.loads(f.read())

counts = {}

for word in data:

    if not word[0] in counts:
        counts[word[0]] = 0

    counts[word[0]] += 1

pp.pprint(counts) 
