## Assignment 7 - Web Scraping

#### Due: 06-19-2023 (Monday @ 10:10 a.m.)

### Overview

Scraping weather from around the world.
https://data.library.virginia.edu/getting-started-with-web-scraping-in-python/

### Leveraging a URL

- `https://www.wunderground.com/history/`
- `https://www.wunderground.com/history/daily/KLAW/date/2023-6-13`
- `https://www.wunderground.com/history/weekly/KLAW/date/2023-6-13`
- `https://www.wunderground.com/history/monthly/KLAW/date/2023-6`

If you look at the url's above, you can see small variations in the path for each item. The first part of the url remains consistent which is very typical. The parts are:

1. protocol: `https`
2. subdomain: `www`
3. domain name: `wunderground.com`
4. path: everything after the domain name

If you remove the subdomain `www` and load `https://wunderground.com/history`, you should find that it won't matter. The site will redirect you to `https://www.wunderground.com/history` anyway. I'm not sure why sites still insist on using `www` as part of the url since its basically inherent in being on the web. It used to indicate a "public" facing portion of a site, but I really do not think that is the case nowadays. I guess it's there for legacy or seo reasons. Anyway, I digress.

It seems that the `history` keyword (path or folder) leads us to a page that allows us to "query" the site simply by placing the correct values after that keyword. These same keywords can be discovered by using the given form on the history page by allowing us to search based on zip code. However, I noticed that there were three basic query types:

1. daily
2. weekly
3. monthly

These three query params were followed by an `airport code` (in this case `KLAW` since I searched using 76308) and a date. So, my guess would be that wunderground gets specific weather based on airport codes, which is pretty normal since most airports have interest in the weather and doppler radar, and then filters the request based on the date passed in via the url. The `daily` and `weekly` dates have "year-month-day" and the monthly date has only "year-month". So, we can build a query for this site simply by knowing the components.

1. protocol: `https`
2. domain: `www.wunderground`
3. base_path: `history`
4. query_type: `[daily, weekly, monthly]`
5. airport_code: (see csv files in this folder)
6. date: `year-month-day`

I also noticed that if you left the date format like this: `2023-6-13` (keeping the day) in a monthly query, it still resulted in the correct page and data to be loaded.

#### Python Examples

We don't need to build the url based on each individual component since the base portion of the url will not change. So I won't be creating variables for protocol for example. I just need to change the `query_type` and the `date`.

```python
base_url = "https://wunderground.com/history"
query_type = "monthly"
airport = "YPJT"
year = "2021"
month = "6"
day = "1"

# build the url to scrape weather from
url = f"{base_url}/{query_type}/{airport}/{year}-{month}-{day}"
# prints: https://www.wunderground.com/history/monthly/YPJT/date/2021-6-1
# gets weather info for Perth Australia
```

### Reading in the Airport Codes

```python
import csv
with open('airport-codes.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['ident'])
```

