from selenium import webdriver

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://ticket.interpark.com')
driver.find_element_by_css_selector("#Nav_SearchWord").send_keys("아이유")
driver.find_element_by_css_selector("#AllSearch > fieldset > div.box > a").click()

# 아래와 같이 css selector를 직접 사용해도 됨
#driver.find_element_by_css_selector("a.btn_search").click()
