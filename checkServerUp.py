__author__ = 'saipc'
import requests
# (480)-703-5615
# server checker for SS Class, can keep track of which teams have deployed
def makeRequest(url):
    try:
        r = requests.get(url, verify=False, timeout=5)
        return r
    except Exception as e:
        print "Timeout"
        return None


def checkIfUp():
    serversUp = []
    for x in xrange(1, 17):
        url = 'https://group' + str(x) + '.mobicloud.asu.edu'
        print url
        r = makeRequest(url)
        if r and r.status_code == 200 and r.headers != None and len(r.text) > 100:
            print "Server is up"
            serversUp.append(x)
        else:
            print "Still down"
    for server in serversUp:
        print "group" + str(server) + " is up"

checkIfUp()