__author__ = 'saipc'

class Alpha(object):
    def __init__(self, a):
        self.x = a
    def printAlpha(self):
        print self.x

class Beta(object):
    def __init__(self, a, b):
        self.p = a
        self.q = self.p + b
    def printBeta(self):
        print self.p, self.q

class Gamma(Alpha, Beta):
    def __init__(self, a, b, c):
        Alpha.__init__(self, a)
        Beta.__init__(self, c, 0)


a = 5
b = 10
c = 10.3

x = Gamma(a, b, c)
x.printAlpha()
x.printBeta()