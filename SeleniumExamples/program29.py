from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfF7VHHo_Uu35_jA7rhyeikUrkVoz7t4wyFAwn6lKzBCzZrJw/viewform?c=0&w=1")
browser.find_element_by_name("entry.712063927").send_keys("hacktrickconf")
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input").send_keys("hacktrickconf@conf.com")
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div/div[2]").click()
time.sleep(5)
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[3]/div[2]/div/content/div/label[4]/div").click()
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div[2]/div/content/div/label[1]").click()
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div[2]/content/span").click()
