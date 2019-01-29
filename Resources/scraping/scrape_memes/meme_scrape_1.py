from beautifulscraper import BeautifulScraper
scraper = BeautifulScraper()

url = "https://ifunny.co"
page = scraper.go(url)

# find all of the links to each category (other pages)
# they happen to be in line item (li) tags
for li in page.find_all("li",{"class":"categories-list__item"}):
    print(li)
    print(li.a)
    print(li.a['href'])
    print("%s%s" % (url,li.a['href']))
    sub_url = url+li.a['href']
    sub_page = scraper.go(sub_url)

    for sli in sub_page.find_all("li",{"class":"categories-list__item"}):
        print(sli.a['href'])