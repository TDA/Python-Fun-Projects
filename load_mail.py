__author__ = 'saipc'
import os

from mail_reader import read_mails

# the mails in maluser are direct proof of the attack
files = ['normaluser', 'maluser']
# but the mails in normaluser could contain the x-check
# header, if they do, then that is a successful attack
# as well. This is due to pythons way of attaching
# headers, instead of overwriting, it ignores duplicate
# headers, so we need to inject a new one.
NO_INJECTION_FILE = 'reguser'

normal_mails = []
injected_mails = []

# for f in files:
#     # read each and load into memory
#     if (os._exists(f)):
#         with open(f, 'r') as file_handle:
#             mail_data = file_handle.read()

# helper functions
def check_total_mails(filename):
    messages = read_mails(filename)
    return len(messages)

def is_header_present(message, header):
    return message.contains(header)

messages = read_mails('~/reguser')

for m in messages:
    print(m)

    # keys = m.keys()
    # for k in keys:
    #     print("Key: ", k, "Value: ", m.get(k))

