from beautifulscraper import BeautifulScraper
from time import sleep
import sys
import json

scraper = BeautifulScraper()

all_links = []

"""
Given a beautiful soup object, it grabs a line item (li) 
with a specific class.

This function could be made a little more robust. 
(e.g. pass in a tag, with a class or id)
"""
def get_category_links(data):
    categories = []
    for li in data.find_all("li", {"class": "categories-list__item"}):
        categories.append(url+li.a['href'])

    return categories

"""
Adds links to a list ensuring no dups are added.
Not sure if its needed in this case. Being cautious
"""
def add_links(links):
    for link in links:
        if not link in all_links:
            all_links.append(link)


# If file is called directly run this block
if __name__ == '__main__':
    
    url = "https://ifunny.co"
    page = scraper.go(url)
    category_links = get_category_links(page)
    add_links(category_links)

    # Ignore first link (its the home page) using [1:]
    
    for category in category_links[1:]:
        sleep(.02)
        sys.stdout.write('.')
        sys.stdout.flush()
        page = scraper.go(category)
        sub_category_links = get_category_links(page)
        all_links.extend(sub_category_links)
    sys.stdout.write("\n")
    print(all_links)
    print(len(all_links))

    f = open('meme_links.json','w')

    f.write(json.dumps(all_links))
    f.close()
