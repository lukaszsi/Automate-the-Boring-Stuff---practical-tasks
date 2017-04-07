#! python3
# 2048.py - opens website game and automatically gets high score.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Opens website with game.
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# Plays
htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
