from selenium import webdriver

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://ticket.interpark.com')
driver.find_element_by_css_selector("#Nav_SearchWord").send_keys("아이유")
driver.find_element_by_css_selector("#AllSearch > fieldset > div.box > a > img").click()

# implicit waits
driver.implicitly_wait(5)
ui = driver.find_element_by_css_selector("#playend_list > tr:nth-child(1) > td.info_Play > div > dl > dt > h4 > a")
print(ui.text)