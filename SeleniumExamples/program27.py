from selenium.webdriver.common.keys import Keys
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://www.google.com.tr")
elem = browser.find_element_by_id("lst-ib")
elem.send_keys("Hacktrickconf 2017")
elem.send_keys(Keys.RETURN)
#browser.close()
