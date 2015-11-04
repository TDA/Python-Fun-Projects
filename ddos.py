__author__ = 'saipc'

__author__ = 'saipc'
import requests
# server checker for SS Class, can keep track of which teams have deployed
def makeRequest(url):
    try:
        r = requests.get(url, verify=False, timeout=0.015)
        return r
    except Exception as e:
        print "Timeout"
        return None


def performDDOS(url, numberOfRequests):
    requestsFailed = []
    requestsSuccessful = []
    for x in xrange(0, numberOfRequests):
        print url
        r = makeRequest(url)
        if r == None:
            requestsFailed.append(x)
        if r and r.status_code == 200 and r.headers != None and len(r.text) > 100:
            print "Server is up"
            requestsSuccessful.append(x)
    for request in requestsFailed:
        print "Failed Request : " + str(request) + " Server not responding"
    print "Total failed requests", len(requestsFailed) , "/", 150

performDDOS("https://group13.mobicloud.asu.edu/SBS/", 150)