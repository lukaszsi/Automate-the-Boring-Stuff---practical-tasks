#! python3
# linkVerification.py - program attempts to download every link on page and gives
# information if link is broken.

import requests
import bs4
import os

webPage = input('What address should I check? ')
res = requests.get(webPage)
res.raise_for_status()
soupObj = bs4.BeautifulSoup(res.text, 'lxml')
elements = soupObj.select('a[href]')
print('Amount of elements: ' + str(len(elements)))
for count, element in enumerate(elements):
    if element.get('href').startswith('http'):
        checkElem = element.get('href')
    else:
        checkElem = os.path.dirname(webPage) + '/' + element.get('href')
    try:
        elemRes = requests.get(checkElem)
    except:
        print('This element can not be checked! ' + str(element.get('href')))
        continue
    if elemRes.status_code == 404:
        print(checkElem + ' has 404 status code!')
    else:
        continue
print('All elements checked.')
