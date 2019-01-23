## Data Scraping - Python Beautiful Soup
### Due: TBD

- https://www.datacamp.com/community/tutorials/web-scraping-using-python
- https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
- https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know


```sh
pip install beautifulscraper
```

```python
from beautifulscraper import BeautifulScraper
scraper = BeautifulScraper()

body = scraper.go("https://ifunny.co/")

# find all of the links to each category (other pages)
for li in page.find_all("li",{"class":"categories-list__item"}):
    print(li)

page.find_all("img",{"class":"media__image"})
```