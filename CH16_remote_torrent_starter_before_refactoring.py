#! python3

# remoteTorrentStarter.py - checks email account every 15 minutes for any
# instructions you mail it and executes those instructions automatically
# and sends you an email about starting task and about closing the torrent program.

import time, imapclient, pyzmail, datetime, subprocess, smtplib, logging
from backports import ssl

logging.basicConfig(filename='emailTorrent3Log.txt', level=logging.DEBUG, 
		 format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
def emailTorrent():
    logging.debug('Starting IMAP connection')
    dayAgo = datetime.datetime.now() - datetime.timedelta(days=1)
    timeString = dayAgo.strftime('%d-%b-%Y')
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True, ssl_context=context)
    imapObj.login('test@gmail.com', 'password')
    imapObj.select_folder('INBOX', readonly=False)
    UIDs = imapObj.search('SINCE ' + timeString)
    logging.debug('Number of new messages: ' + str(len(UIDs)))
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    for uid in UIDs:
        message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
        if message.text_part != None:
            msgText = message.text_part.get_payload().decode(message.text_part.charset)
            if '4x567' in message.get_subject():
                logging.debug('Message with password detected')
                torrentProcess = subprocess.Popen(['C:\Program Files (x86)\BitLord\BitLord.exe', msgText])
                imapObj.delete_messages(uid)
                sendMail('started: ' + msgText)
                logging.debug('Message with start info sent')
                torrentProcess.wait()
                sendMail('finished: ' + msgText)
                logging.debug('Message with end info sent')
    imapObj.logout()

def sendMail(info):
    logging.debug('Starting SMTP connection')
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('test@gmail.com', 'password')
    msg = '''Subject:Task\n
Task ''' + info + ''' .'''
    smtpObj.sendmail('test@gmail.com', 'otherone@gmail.com', msg)
    smtpObj.quit()
    

while True:
    emailTorrent()
    logging.debug('Waiting 15 minutes')
    for i in range(900):
        time.sleep(1)
