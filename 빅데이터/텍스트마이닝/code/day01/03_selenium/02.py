from selenium import webdriver

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')
driver.find_element_by_css_selector("#PM_ID_serviceNavi > li:nth-child(9) > a").click()


