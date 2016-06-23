__author__ = 'saipc'

with open('allspammingips') as f:
    h = dict()
    for line in f.readlines():
        h[line] =  h.get(line, 0) + 1

    print(h)
    count = 0
    for key in h.keys():
        if (h.get(key) > 1):
            count += 1
    print(count)