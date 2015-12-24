__author__ = 'saipc'
import re
import os

regex = re.compile(r"Sai Pc: ((.*)(\.|\,){1,}\n){4,}", re.IGNORECASE)

path = "/Users/schandramouli/Downloads/Whatsapp Chats"

os.chdir(path)
files = os.listdir(".")

for file in files:
    with open(file) as file:
        content = file.read()
        matches = re.search(regex, content)
        if matches:
            print file, matches.groups()