import time
from selenium import webdriver
import os
import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)

driver.get('https://www.coinbase.com/price/bitcoin')
time.sleep(5) # Let the user actually see something!
	
element = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/span").getAttribute("value")
#cost = int(driver.find_element_by_class_name("currency-price-wrapper").getAttribute("currency-price"))
print((element))
#driver.execute_script('window.location.replace()')

time.sleep(10) # Let the user actually see something!
driver.quit()

