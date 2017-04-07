#! python3
# sendMail.py - programm for automatically sending e-mails
import sys
import time
from selenium import webdriver

# Check if sys.argv has < 3 arguments, if yes, you do not have
# enough data to continue
if len(sys.argv) < 3:
    print('Not enough data, sorry!')

# sys.argv[1] is your mail address, ' '.join (sys.argv [2:]) is
# your string to send as e-mail text
address = sys.argv[1]
message = ' '.join(sys.argv [2:])

# login to gmail (html version) with selenium
browser = webdriver.Firefox()
browser.get('https://mail.google.com/mail/u/0/h/1pq68r75kzvdr/?v%3Dlui')
emailUser = browser.find_element_by_id('Email')
emailUser.send_keys('example')
emailUser.submit()
time.sleep(3)
emailPass = browser.find_element_by_id('Passwd')
emailPass.send_keys('examplepassword')
emailPass.submit()
time.sleep(15)

# create new email with information aquired from sys.argv and send it
newMsg = browser.find_element_by_partial_link_text('Napisz wiadom')
newMsg.click()
addressWindow = browser.find_element_by_id('to')
addressWindow.send_keys(address)
msgWindow = browser.find_element_by_class_name('mi')
msgWindow.send_keys(message)
sendButton = browser.find_element_by_name('nvp_bu_send')
sendButton.click()
