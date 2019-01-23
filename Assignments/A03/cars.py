#!/usr/local/bin/python3

from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
import json
import sys
from time import sleep
from random import shuffle

scraper = BeautifulScraper()

elements = []

pages = [x+1 for x in range(5)]

f = open("car_data.json","w")
car_data = {}

delays = [.01,.02,.03,.04,.05]

for i in pages:
    url = "https://www.cnet.com/roadshow/pictures/"+str(i)+"/"

    page = scraper.go(url)

    divs = page.find_all('div',{"class":"col-3"})

    for div in divs[1:]:
        print(div.a.figure.img['src'])
        parts = div.a.figure.img['src'].split("/")
        urllib.request.urlretrieve(div.a.figure.img['src'], 'car_images/'+parts[-1])
        car_data[parts[-1]] = div.a.p.text.strip()
        shuffle(delays)
        sleep(delays[0])

f.write(json.dumps(car_data))

pprint(car_data)