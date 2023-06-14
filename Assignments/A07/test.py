import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver

import time

def rendering(url):
    
        # change '/usr/local/bin/chromedriver' to the path 
        # from you got when you ran 'which chromedriver'
        driver = webdriver.Chrome('/usr/local/bin/chromedriver') # run ChromeDriver
        driver.get(url)                                          # load the web page from the URL
        time.sleep(3)                                            # wait for the web page to load
        render = driver.page_source                              # get the page source HTML
        driver.quit()                                            # quit ChromeDriver
        return render                                            # return the page source HTML
    
if __name__=='__main__':

    url = 'http://www.wunderground.com/history/daily/KCHO/date/2020-12-31'

    # Create a selenium-wire webdriver instance
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Make A GET request
    driver.get(url)
    # Print some underlying HTTP request data
    print(driver.requests[0].headers, driver.requests[0].response)

