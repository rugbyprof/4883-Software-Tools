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
        # add a small delay so you don't hammer the server
        sleep(.02)

        # show progress by printing a dot to the screen
        sys.stdout.write('.')
        sys.stdout.flush()

        # grab the category page
        page = scraper.go(category)

        # get a list of sub categories
        sub_category_links = get_category_links(page)

        # append would create a list of lists where extend just adds
        # items keeping a single list of items
        all_links.extend(sub_category_links)
    sys.stdout.write("\n")
    print(all_links)
    print(len(all_links))

    # write all of our links to a json file
    f = open('meme_links.json','w')
    f.write(json.dumps(all_links))
    f.close()
