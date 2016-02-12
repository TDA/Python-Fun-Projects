__author__ = 'saipc'
import requests
from bs4 import BeautifulSoup
# http://www.rhymezone.com/r/rhyme.cgi?typeofrhyme=perfect&Word=word&loc=spellmap3

def extract_words(link):
    print(link)
    link = BeautifulSoup(link, 'html.parser')
    print(link)

def find_words(word):
    words = []
    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'Host' : 'www.rhymezone.com',
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    }
    r = requests.get("http://www.rhymezone.com/r/rhyme.cgi?typeofrhyme=perfect&Word=" + word, headers=headers)

    print(r.status_code)
    # print(r.text)
    html = BeautifulSoup(r.text, 'html.parser')
    # print(html)
    words_links = html.findAll('a', "r")
    words = map(extract_words, words_links)
    return words

find_words("sai")