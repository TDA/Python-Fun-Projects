__author__ = 'saipc'
import random
import pyperclip
import os

def wish(name):
    return 'Happy Birthday ' + name

print(wish('Sai'))

def thank(name):
    thank_yous = ['Thank you so much', 'Thank you very much', 'Thank you!!']
    smileys = [':)', ':D', ';)']
    return_wishes = ['Hope you are doing well!', 'What are you upto?', 'Hope you are doing great', 'Take care!']

    return random.choice(thank_yous) + \
           ' @' + name + ' ' + \
           (random.choice(smileys) + random.choice(smileys)) + ' ' + \
           random.choice(return_wishes) + ' ' + \
           random.choice(smileys)

# add list of ppl here from the html extracted from fb
# that way this can generate the required thank you notes
if __name__ == '__main__':
    with open('BDayFilterResults', 'r') as f:
        for line in f:
            print(thank(line))