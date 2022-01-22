from googlesearch import search
from urllib.request import urlopen
import time
import bs4

searchKeyword = input("Please input your search keyword: ")
print()
searchSites = ['www.straitstimes.com', 'www.todayonline.com']

def findTitle(url):
    webpage = urlopen(url).read()
    title = str(webpage).split('<title>')[1].split('</title>')[0]
    return title

for site in searchSites:
    query = searchKeyword + " site:\"" + site + "\""
    for link in search(query, tld="com.sg", num=5, stop=5, pause=2):
        print(findTitle(link))
        html = urlopen(link).read().decode('utf-8')
        soup = bs4.BeautifulSoup(html, 'html.parser')
        print(link)
        results = soup.find(text=lambda value: value and searchKeyword in value)
        print(results)

        time.sleep(5)
        print()
        
