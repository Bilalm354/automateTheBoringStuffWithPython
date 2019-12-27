# amazon.py - Opens several Google search results.
# !!!! Doesn't work
import requests, sys, webbrowser, bs4

print ('Amazoning...') # display text while downloading the Google page

res = requests.get('https://www.amazon.co.uk/s?k=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# TODO: Open a browser tab for each result.
link_elems = soup.select('a')
str(link_elems[0])
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://www.amazon.co.uk' + link_elems[i].get('href'))
