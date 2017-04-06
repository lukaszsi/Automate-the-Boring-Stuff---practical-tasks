#! python3
#downloadTwoThreadsContinue.py - Checks daily if there is  and downloads every new XKCD and GWTBW comic in separate threads.

import requests, os, bs4, time, sys, shelve, logging, threading

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

listOfcomicsData = [['http://www.blastwave-comic.com/', 'center img',
                     'http://www.blastwave-comic.com/', 'gwtbwData'],
                    ['http://xkcd.com', '#comic img', 'http:', 'xkcdData']]

# creates folder to store comics there
logging.debug('Creating folder for comics')
os.makedirs('Comics', exist_ok = True)
    
# checks if it is more than ~24h/day from last start, if yes continues, if no, closes
if 'timeData.dat' in os.listdir():
    shelveFile = shelve.open('timeData')
    openingTime = shelveFile['openingTime']
    logging.debug('Checking when the program was opened last time')
    if time.time()- openingTime < 86350:
        logging.debug('Program was opened less than 24hrs ago, closing')
        shelveFile.close()
        sys.exit()
    
def comicFunction(url, comicElemSoup, comicUrlPart, comicData):
    # opens main page of comic, checks the comic img source, if it is different from what
    # is in database, downloads it
    logging.debug('Opening the main page of comic')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4. BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select(comicElemSoup)
    if comicElem == []:
        logging.debug('No comic on site. Closing')
        sys.exit()
    else:
        getStr = comicElem[0].get('src')
        if getStr.startswith('.'):
            getStr = getStr[1:]
        comicUrl = comicUrlPart + getStr
    if comicData + '.txt' in os.listdir():
        fileData = open(comicData + '.txt')
        if fileData.read() == comicUrl:
            logging.debug('Comic is still the same, closing')
            fileData.close()
            sys.exit()
        
    logging.debug('Writing comic to a file')
    res = requests.get(comicUrl)
    res.raise_for_status()
    imageFile = open(os.path.join('Comics', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # changes url data in database
    logging.debug('Changing url data in database')
    fileData = open(comicData + '.txt', 'w')
    fileData.write(comicUrl)
    fileData.close()

    # closes
    logging.debug('End of thread, closing')

downloadThreads = []

for list in listOfcomicsData:
    downloadThread = threading.Thread(target=comicFunction, args=list)
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
# wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
    
# changes time data in database
logging.debug('Changing time data in database')
shelveFile = shelve.open('timeData')
openingTime = time.time()
shelveFile['openingTime'] = openingTime
shelveFile.close()
logging.debug('End of program')
