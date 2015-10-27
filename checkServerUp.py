__author__ = 'saipc'
import requests
# server checker for SS Class, can keep track of which teams have deployed
def makeRequest(url):
    try:
        r = requests.get(url, verify=False, timeout=5)
        return r
    except Exception as e:
        return None


def checkIfUp():
    serversUp = []
    for x in xrange(1, 15):
        url = 'https://group' + str(x) + '.mobicloud.asu.edu'
        print url
        r = makeRequest(url)
        if r and r.status_code == 200 and r.headers != None and len(r.text) > 100:
            print "Server is up"
        else:
            print "Still down"

checkIfUp()