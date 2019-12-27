#! /usr/bin/env python3
# lucky.py = Opens several google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top seach result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select(".r a") # not sure if this will work (try . r)
print(str(linkElems[0]))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

