from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import json
import sys

def canBeInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

f = open("sheet001.html", 'r')
s = f.read()
soup = BeautifulSoup(s,"lxml")

rows = soup.find_all('tr')

f = open("nfl_stats_ids.json","w")

stats = {}

keys = ['Name', 'Comment']

for row in rows:
    vals = []
    cols = row.find_all('td')
    for col in cols:
        if canBeInt(col.text):
            vals.append(col.text)
        else:
            if col.text != "":
                vals.append(col.text.replace("\n","").replace(u'\xa0', u' ').replace(u'  ', u' '))
    if len(vals) > 0 and canBeInt(vals[0]):
        stats[int(vals[0])] = dict(zip(keys, vals[1:]))

print(stats)

f.write(json.dumps(stats, sort_keys=True))
