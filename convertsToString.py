def convertsToString(list):
    newString = ''
    for i in range(len(list)-1):
        newString += list[i] + ', '
    newString += 'and ' + list[-1]
    return newString

spam = ['apples', 'bananas', 'tofu', 'cats']
print(convertsToString(spam))
