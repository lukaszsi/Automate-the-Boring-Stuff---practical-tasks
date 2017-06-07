#! python3
''' Script works same as built-in strip() function. It removes
whitespace characters or chars provided through optional argument
from beginning and end of the given string.'''
import re

def customStrip(string, toRemove='\s'):
    beginRegex = re.compile(r'^['+ toRemove+']+')
    string = beginRegex.sub('', string)
    endRegex = re.compile(r'['+ toRemove+']+$')
    string = endRegex.sub('', string)
    return string
