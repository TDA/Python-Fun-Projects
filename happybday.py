__author__ = 'saipc'
import random

def wish(name):
    return 'Happy Birthday ' + name

def thank(name):
    thank_yous = ['Thank you so much', 'Thank you very much', 'Thank you!!']
    smileys = [':)', ':D', ';)']
    return_wishes = ['Hope you are doing well!', 'What are you upto?', 'Hope you are doing great', 'Take care!']

    return random.choice(thank_yous) + \
           ' @' + name + ' ' + random.choice(smileys) + random.choice(smileys) + ' ' + \
           random.choice(return_wishes) + ' ' + \
           random.choice(smileys)

# add list of ppl here from the html extracted from fb
# that way this can generate the required thank you notes
# finished this, but can use pyperclip for c/p
# unfortunately fb doesnt allow js posting anymore :(
if __name__ == '__main__':
    print(wish('Sai'))
    with open('Data/BDayFilterResults.html', 'r') as f:
        for line in f:
            print(thank(line))