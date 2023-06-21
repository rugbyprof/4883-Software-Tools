"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time                                             # needed for the sleep function

from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager


import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        service = Service(executable_path='/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 3 seconds for dynamic data to load...")
        time.sleep(5)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML
    
if __name__=='__main__':

    # Could be a good idea to use the buildWeatherURL function from gui.py
    url = 'http://www.wunderground.com/history/daily/KCHO/date/2023-01-01'

    # get the page source HTML from the URL
    #page = asyncGetWeather(url)
    
    with open('weather.html') as f:
        page = f.read()

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    # history = soup.find('lib-city-history-observation')
    
    tables = soup.find_all('table')
    
    
    print(tables[0].text)
    
    rows = tables[0].find_all('tr')
    
    for row in rows:
        content = row.find_all('td')
        for c in content:
            print(c.text.strip().replace(" ","").replace("\n",""))
    

    # print the parsed HTML
    # print(history.prettify())
    
    # with open('weather.html', 'w') as f:
    #     f.write(history.prettify())
    
    # print(len(tables))