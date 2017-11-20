from selenium import webdriver
import contextlib
import math

@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()

with quitting(webdriver.Firefox()) as driver:
    driver.implicitly_wait(30)
    driver.get("https://www.google.com")
    driver.get_screenshot_as_file("google.png")
