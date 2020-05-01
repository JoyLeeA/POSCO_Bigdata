from selenium import webdriver
from bs4 import BeautifulSoup
import time

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://ticket.interpark.com')
driver.find_element_by_css_selector("#Nav_SearchWord").send_keys("아이유")
driver.find_element_by_css_selector("#AllSearch > fieldset > div.box > a > img").click()

time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')
result = soup.select("#playend_list > tr:nth-of-type(1) > td.info_Play > div > dl > dt > h4 > a")
for r in result:
    print(r.text)