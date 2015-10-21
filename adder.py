__author__ = 'saipc'

def sumOfIntegers(arr):
    n = len(arr)
    sum = 0
    for i in xrange(0, n):
        x = arr[i]
        sum += x
    return sum

print sumOfIntegers([1, 2, 3, 4])
print sum([1, 2, 3, 4])

if __name__ == '__main__':
    n = int(raw_input())
    string = raw_input()
    arr = string.split(" ")
    intarr = [int(x) for x in arr]
    print sum(intarr)