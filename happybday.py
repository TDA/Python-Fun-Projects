__author__ = 'saipc'
import random

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

for i in xrange(5):
    print(thank('sai'))