__author__ = 'saipc'

n = int(raw_input())
s1 = ""
for i in xrange(0, n):
    s1 = " " * (n - i - 1) + "#" * (i + 1)
    print s1

def sumOfIntegers(arr):
    n = len(arr)
    sum = 0
    for i in xrange(0, n):
        x = arr[i]
        sum += x
    return sum
