#! /usr/bin/python3
# lucky.py - one click, multiple tab google search

import requests, sys, webbrowser, bs4

print('Googling...')
r = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
r.raise_for_status()

# retrives top search result links
soup = bs4.BeautifulSoup(r.text)

#opens a tab for each search result
links = soup.select('.r a')
numOpen = min(5, len(links))
for i in range(numOpen):
    webbrowser.open('http://google.com' + links[i].get('href'))