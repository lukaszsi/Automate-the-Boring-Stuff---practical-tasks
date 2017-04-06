#! python3
# umbrellaRemainder.py - checks if it's gonna be raining and sends
# an email about it.
import smtplib, requests, bs4, sys, datetime, time

# Check if it is about 7 o'clock.
while datetime.datetime.now().hour != 7:
    for i in range(600):
        time.sleep(1)

# Parse webpage.
res = requests.get('https://pogoda.interia.pl/prognoza-szczegolowa-wroclaw,cId,39240')
res.raise_for_status()
weatherSoup = bs4.BeautifulSoup(res.text, 'lxml')
rainElement = weatherSoup.select('div .weather-currently-icon-description')
if 'Deszcz' in rainElement[0].text:
    msg = '''Subject: Rain\n
Siema, dziś pada, weź parasol!'''.encode('utf-8')
else:
    msg = '''Subject: Rain\n
Siema, dziś nie pada, nie bierz parasola.'''.encode('utf-8')

# Send e-mail.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('test@gmail.com', 'password')
smtpObj.sendmail('test@gmail.com', 'myemail@gmail.com', msg)
smtpObj.quit()
