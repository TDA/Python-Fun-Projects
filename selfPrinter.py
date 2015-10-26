__author__ = 'saipc'

def selfPrinter(fileName):
    with open(fileName) as file:
        print file.read()


selfPrinter('selfPrinter.py')
