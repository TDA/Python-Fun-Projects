__author__ = 'saipc'


import requests
import random

def genAutoFormRequests(url):
    fname = ""
    for x in xrange(0, 4):
        fname = fname + random.choice(['a', 'b', 'c', 'd', 'e'])
    for x in xrange(0, 4):
        fname = fname + random.choice(['1', '2', '3', '4', '5'])
    print fname
    payload = {
        'fname': fname,
        'lname': fname,
        'desname': 'reg',
        'address': 'some rand addr',
        'Phno': '1234567890',
        'email':'saiprash_thegreatest@yahoo.co.in',
        'username': fname,
        '_csrf':'4f52f7bd-2b50-4209-882a-68c7ec67fb48'
    }

    with requests.Session() as s:
        s.cookies = requests.utils.cookiejar_from_dict({'JSESSIONID':'45F4447C927F328E0129482ECB6E0285'})
        r = s.post(url, verify=False, data=payload)
        print r.text
        print r.status_code
        print r.cookies

if __name__ == '__main__':
    genAutoFormRequests('https://group1.mobicloud.asu.edu/SBS/NewRegUser')

    #_csrf:"f9c75c24-4271-4718-a306-32ff18c9a8f1"
    #tran:"Modify"