__author__ = 'saipc'

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("google.com", 80))

s.send("GET / HTTP/1.0\r\n\r\n")

while 1:
    buf = s.recv(1000)
    if not buf:
        break
    print buf

s.close()
