from beautifulscraper import BeautifulScraper
from pprint import pprint
scraper = BeautifulScraper()

url = "http://www.hubertiming.com/results/2017GPTR10K"
page = scraper.go(url)

table = page.find('table',{"id":"individualResults"})

headers = table.thead

data = []
categories = []

print(headers)

for th in headers.find_all('th'):
    categories.append(th.text)

for tr in table.tbody.find_all('tr'):
    temp = {}
    i = 0
    for td in tr.find_all('td'):
        temp[categories[i]] = td.text
        i += 1
    data.append(temp)

pprint(data)