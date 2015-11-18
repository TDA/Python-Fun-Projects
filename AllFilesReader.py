__author__ = 'saipc'

import os
import re

def readAllFiles(dirName):
    os.chdir(dirName)
    files = os.listdir(".")
    for file in files:
        if os.path.isfile(file):
            with open(file, "r") as fileOpener:
                data = fileOpener.read()
                if (re.search("\((\d{3})\)-(\d{3})-\d{4}", data)):
                    print file


readAllFiles('.')
