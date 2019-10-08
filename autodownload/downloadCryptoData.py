import time
from selenium import webdriver
import os
import sys

iterationsize=int(input('iteration size: '))
downloadpath=input('path to download: ')
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : downloadpath}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("chromedriver.exe",chrome_options=chromeOptions)  # Optional argument, if not specified will search path.
driver.get('https://markets.businessinsider.com/currencies/btc-usd');
time.sleep(5) # Let the user actually see something!

filesdownloaded=len(os.listdir(downloadpath))
for x in links[0:(iterationsize)]:
    driver.execute_script('window.location.replace("https://www.opensubtitles.org/en/subtitleserve/sub/{}")'.format(x))
    time.sleep(3)
    filesdownloadedcache=len(os.listdir(downloadpath))
    print(x)
    if filesdownloaded == filesdownloadedcache:
        print('error file at: '+x)
        input('')
        driver.quit()
        sys.exit()
    filesdownloaded=filesdownloadedcache
time.sleep(10) # Let the user actually see something!
driver.quit()

