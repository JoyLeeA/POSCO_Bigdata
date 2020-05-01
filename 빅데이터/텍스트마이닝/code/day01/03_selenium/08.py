from selenium import webdriver
from bs4 import BeautifulSoup

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.investing.com/indices/us-spx-500')
ui = driver.find_element_by_css_selector("#leftColumn > div:nth-child(20) > article:nth-child(3) > div.textDiv > a")
print(ui.text)
ui = driver.find_element_by_css_selector("#leftColumn > div:nth-child(20) > article:nth-child(4) > div.textDiv > a")
print(ui.text)
ui = driver.find_element_by_css_selector("#leftColumn > div:nth-child(20) > article:nth-child(5) > div.textDiv > a")
print(ui.text)

