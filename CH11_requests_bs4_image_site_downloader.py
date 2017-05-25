#! python3
# imageSiteDownloader2.py - downloads all searched photos from website

import os
import requests
import bs4

os.chdir('C://Python')
os.makedirs('Cats', exist_ok=True)

# Parses webpage with photos
res = requests.get('https://www.dreamstime.com/search.php?securitycheck=2b51281fdde22a6b9529c756cb8f1c22&firstvalue=&srh_field=cats&s_ph=y')
res.raise_for_status()
soupObj = bs4.BeautifulSoup(res.text, 'lxml')
elements = soupObj.select('.bigthumb')
for count, element in enumerate(elements):
    imageLink = element.get('src')
    imageFile = open(os.path.join('Cats', os.path.basename(imageLink)), 'wb')
    imgRes = requests.get(imageLink)
    imgRes.raise_for_status()
    for chunk in imgRes.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
