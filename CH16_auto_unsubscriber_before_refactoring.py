#! python3
# autoUnsubscriber.py - automatically searches your e-mails and opens links
# to unsubscribe.

import imapclient, pyzmail, bs4, webbrowser, os, datetime
from backports import ssl

# Checking what was the date one mont ago
monthAgo = datetime.datetime.now() - datetime.timedelta(days=30)
timeString = monthAgo.strftime('%d-%b-%Y')
searchTimeStr = 'SINCE ' + timeString

# Logging to the e-mail account.
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True, ssl_context=context)
imapObj.login('example@gmail.com', 'password')
imapObj.select_folder('INBOX', readonly=True)

# Searching for all the e-mails from last month.
UIDs = imapObj.search(searchTimeStr)
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

# Parsing every e-mail text.
urlsList = []
for uid in UIDs:
    message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
    if message.html_part != None:
        text = message.html_part.get_payload().decode(message.html_part.charset)
        soupFile = bs4.BeautifulSoup(text, 'lxml')
        linksList = soupFile.select('a[href]')
        for link in linksList:
            if 'unsubscribe' in link.get('href'):
                if os.path.dirname(link.get('href')) not in str(urlsList):
                    urlsList.append(link.get('href'))
imapObj.logout()
# Opening all the links to unsubscribe.
for link in urlsList:
    webbrowser.open(link)

