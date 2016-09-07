__author__ = 'saipc'


def reverse(string):
    return string[::-1]


s = "Sai is a boy"
words = s.split(" ")
rev_words = []
for w in words:
    rev_words.append(reverse(w))
print ' '.join(rev_words)
