__author__ = 'saipc'

# (480)-703-5615

n = int(raw_input())
s1 = ""
# <3 python for the * strings
for i in xrange(0, n):
    s1 = " " * (n - i - 1) + "#" * (i + 1)
    print s1
