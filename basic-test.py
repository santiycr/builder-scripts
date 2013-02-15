from selenium.webdriver.firefox.webdriver import WebDriver
wd = WebDriver()
wd.implicitly_wait(60)
wd.get("https://encrypted.google.com/")
wd.find_element_by_id("gbqfq").click()
wd.find_element_by_id("gbqfq").clear()
wd.find_element_by_id("gbqfq").send_keys("santiago suarez ordoñez")
wd.find_element_by_xpath("//ol[@id='rso']//em[.='Santiago Suarez Ordoñez']").click()
wd.close()
