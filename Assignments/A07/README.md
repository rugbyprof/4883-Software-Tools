## Assignment 7 - Web Scraping

#### Due: 06-19-2023 (Monday @ 10:10 a.m.)

### Background

The initial web scraping example I went over in class was a simple BS4 (beautiful soup) example that scraped tabular data from an NBA page and save it locally in a json formatted file. A link to this code is here: [4883-summer23-scraping](https://replit.com/@rugbyprof/4883-summer23-scraping). I think we all could appreciate the power of scraping a web page to create a local database of collected data. Even though we only saved the information as json, we are not limited to just that format. The NBA page we accessed was statically loaded, meaning that it was created in its entirety on the server, and then sent to our browser. This allowed us to use `python requests` to grab that static page and process it. This is not always the case.

The issue with the site that we want to grab weather data from (`https://www.wunderground.com/history/`) is that the data is loaded **dynamically** / **asynchronously**. This means that the page is not completely created on the server and then sent in its entirety upon the initial request. It means that the initial page load does not include the weather data, and the resulting page that makes it to the requesting browser makes an additional request to load the weather data. As a result, using `python requests` will not get us the data we are looking for, as it only receives the initial response. The additional request is never received by the `requests` library, and thus we are forced to take a different approach.

The approach we will emulate can be read about here: https://data.library.virginia.edu/getting-started-with-web-scraping-in-python/. It describes using selenium to obtain the dynamic data, since selenium allows the programmer to add a delay in waiting for the response. The entire tutorial is really well written, but it fell short due to library updates. Meaning, I could not get it to run since the version of `selenium` and `webdriver` that I installed were new and changed vs the versions used by the author. I managed to fix those issues and have included examples in this assignment folder.

### Overview

This project will combine a `python GUI` with a `beautiful soup web scraper` to: 1. grab, 2. save and 3. display the data. The initial python gui will be used to enter the appropriate values to allow you to leverage the URL, meaning it will accept values for: month, day, year, airport code, and one of the following: daily, weekly, monthly. The resulting python gui will display the received data in a tabular format. PySimpleGui has methods to help with all of this: [Documentation](https://www.pysimplegui.org/en/latest/), [Examples and Demos](https://www.pysimplegui.org/en/latest/#some-examples).

I have include some starter code that can be viewed in the `get_weather` file and the `gui` file. The `airport-codes` file is to help with populating the gui drop down dealing with choosing a location.

|  #  | name                                     | Description                                                      |
| :-: | :--------------------------------------- | :--------------------------------------------------------------- |
|  1  | [airport-codes.csv](./airport-codes.csv) | Necessary data for your gui                                      |
|  2  | [get_weather.py ](./get_weather.py)      | Example selenium async request to grab weather data              |
|  3  | [gui.py](./gui.py)                       | Example gui form to get necessary data to query the weather page |

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

#### Url Building

We don't need to build the url based on each individual component since the base portion of the url will not change. So I won't be creating variables for protocol for example. I just need to change the `filter` and the `date`.

```python
base_url = "https://wunderground.com/history"
filter = "monthly"
airport = "YPJT"
year = "2021"
month = "6"
day = "1"

# build the url to scrape weather from
url = f"{base_url}/{filter}/{airport}/{year}-{month}-{day}"
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

### Summary

- Use PySimpleGui to create a data entry form that includes day, month, year, airport, and filter (daily,weekly,monthly)
- Submit your form which will create the appropriate URL to query wunderground for the specified weather data.
- Use selenium to obtain the async data sent back from wunderground.
- Use BS4 to parse the data and pull out the requested data.
- Finally, use PySimpleGui tabular view to display the data received from the initial request.

### Deliverables

- Create a folder called `A07` to place your assignment files in.
- Update the given python code to work for your own solution, but include all python code that you write in this folder.
- Include in your `README` at least three example queries.
- The example queries should include a screen shots of the initial form GUI (where you enter date, etc.) and a screenshot of the resulting GUI that displays the tabular data resulting from your query ([table example](https://pysimplegui.trinket.io/demo-programs#/tables/the-table-element))
- Look [HERE](../../Resources/01-Readmees/README.md) for information on creating good README's for your projects.
