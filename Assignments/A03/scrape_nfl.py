from beautifulscraper import BeautifulScraper
from pprint import pprint
scraper = BeautifulScraper()

url = "http://www.nfl.com/schedules/2009/REG1"
page = scraper.go(url)

divs = page.find_all('div',{"class":"schedules-list-content"})

print(divs)

for div in divs:
    if "type-reg" in div:
        print(div)

