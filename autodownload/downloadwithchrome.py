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
driver.get('https://www.opensubtitles.org/en/search/subs');
time.sleep(5) # Let the user actually see something!
startatf=open('downloadat.txt','+r')
startat=startatf.read()
startatf.close()
if startat == '':
    startat=0
else:
    startat=int(startat)
file=open('links.txt','r')
links=file.read()
links=links.split('\n')
file.close()
filesdownloaded=len(os.listdir(downloadpath))
for x in links[0+startat:(startat+iterationsize)]:
    driver.execute_script('window.location.replace("https://www.opensubtitles.org/en/subtitleserve/sub/{}")'.format(x))
    time.sleep(3)
    filesdownloadedcache=len(os.listdir(downloadpath))
    print(x)
    if filesdownloaded == filesdownloadedcache:
        print('error file at: '+x)
        for y in range(len(links)):
            if links[y] is x:
                file=open('downloadat.txt','+w')
                file.write(str(y))
        input('')
        sys.exit()
    filesdownloaded=filesdownloadedcache
time.sleep(10) # Let the user actually see something!
driver.quit()
file=open('downloadat.txt','+w')
file.write(str(startat+iterationsize))
file.close()
