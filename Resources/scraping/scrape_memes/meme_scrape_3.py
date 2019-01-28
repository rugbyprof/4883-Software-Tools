from beautifulscraper import BeautifulScraper
from time import sleep
import sys
import json
from pprint import pprint
import urllib

scraper = BeautifulScraper()


def get_category_links(data):
    categories = []
    for li in data.find_all("li", {"class": "categories-list__item"}):
        categories.append(url+li.a['href'])

    return categories

# If file is called directly run this block
if __name__ == '__main__':
    url = 'https://ifunny.co'

    with open('meme_links.json') as f:
        data = json.load(f)

    pprint(data)

    page_nums = [x for x in range(5)]

    for num in page_nums:
        num += 1
        sys.stdout.write(str(num)+' ')
        sys.stdout.flush()
        page = scraper.go('https://ifunny.co/tv-shows/smurfs/page'+str(num)+'?filter=meme')
        
        images = page.find_all('img',{"class":"grid__image"})
        
        for image in images:
            print(image["data-src"])
            parts = image["data-src"].split("/")
            urllib.urlretrieve(image["data-src"], 'meme_images/'+parts[-1])
        


