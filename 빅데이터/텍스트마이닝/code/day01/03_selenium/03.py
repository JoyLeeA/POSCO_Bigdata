from selenium import webdriver

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')
driver.find_element_by_css_selector("#query").send_keys("방탄소년단")


