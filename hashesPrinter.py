__author__ = 'saipc'

n = int(raw_input())
s1 = ""
for i in xrange(0, n):
    s1 = " " * (n - i - 1) + "#" * (i + 1)
    print s1
