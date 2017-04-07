#! python3
# imageSiteDownloader.py - downloads all searched photos from website

import time, os, requests
from selenium import webdriver

os.chdir('C://Python')
os.makedirs('Cats', exist_ok=True)

# Opens webpage with photos
browser = webdriver.Firefox()
browser.get('https://www.dreamstime.com/')


# Searches for category
searchBox = browser.find_element_by_id('srh_field')
searchBox.send_keys('cats')
searchBox.submit()
time.sleep(3)

# downloads resulting images
catsWebdriverObj = browser.find_elements_by_class_name('bigthumb')
linksList = []
for elem in catsWebdriverObj:
    linksList.append(elem.get_attribute('src'))
for i in range(len(linksList)):
    imageFile = open(os.path.join('Cats', os.path.basename(linksList[i])), 'wb')
    res = requests.get(linksList[i])
    res.raise_for_status()
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

