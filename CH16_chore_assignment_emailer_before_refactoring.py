#! python3
# choreAssignmentEmailer21.py - randomly assigns chores to persons and sends them e-mails about it.

import random, smtplib, shelve, time, sys, os

def makeNewChores(peopleAndLastChores):
    # Creating new data.
    peopleAndNewChores = {}
    chores = []
    for person in peopleAndLastChores:
        chores.append(peopleAndLastChores[person][1])
        
    newChores = []
    people = []

    # Here I fulfill list of new chores and list of people, new chores for new people will have
    # the same index in both lists. I wanted to do it with separate list because of the potential
    # problem of the last person and situation when he/she was left only with his last chore to do.
    # This situation is handled by the next part of program.
    for person in peopleAndLastChores:
        lastChore = peopleAndLastChores[person][1]
        people.append(person)
        while True:
            newChore = random.choice(chores)
            if newChore == lastChore and len(chores) != 1:
                continue
            break
        newChores.append(newChore)
        chores.remove(newChore)

    # This part handles the problem when last person was left with his previous chore. We can safely
    # switch it with any other chore in the list because we know no one else was doing it last time.
    if peopleAndLastChores[people[-1]][1] == newChores[-1]:
        newChores[-1], newChores[0] = newChores[0], newChores[-1]

    # Now we can collect all the data, person and his e-mail address and new chore, in one dictionary.
    for person in people:
        emailAddress = peopleAndLastChores[person][0]
        newChore = newChores[people.index(person)]
        peopleAndNewChores[person] = [emailAddress,newChore]
    return peopleAndNewChores

if __name__ == '__main__':
    # checks if it is more than ~24h/day from last start, if yes continues, if no, closes.
    if 'choreEmailer.dat' in os.listdir():
        shelveFile = shelve.open('choreEmailer')
        openingTime = shelveFile['openingTime']
        if time.time()- openingTime < 604000:
            print('Program was opened earlier than week ago! Closing')
            shelveFile.close()
            sys.exit()
    
    dataDict = {'Paul': ['example@gmail.com', 'vacuum'],
                'Steve': ['example2@gmail.com', 'walk dog'],
                'Brad': ['example3@gmail.com', 'dishes'],
                'Angela': ['example4@gmail.com', 'bathroom']}

    peopleAndNewChores = makeNewChores(dataDict)

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('sendinexample@gmail.com', 'passwordhere')    

    for person in peopleAndNewChores:
        emailAddress = peopleAndNewChores[person][0]
        randomChore = peopleAndNewChores[person][1]
        msg = '''Subject: Chores\n
    Hi '''+person+''', this is your weekly chore: '''+randomChore+'''.'''
        
        smtpObj.sendmail('sendinexample@gmail.com', emailAddress, msg)

    smtpObj.quit()

    # changes time data in database
    shelveFile = shelve.open('choreEmailer')
    openingTime = time.time()
    shelveFile['openingTime'] = openingTime
    shelveFile.close()
