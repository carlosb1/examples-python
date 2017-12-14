#!/usr/bin/python


MAX_DEEP = 2

results = []
def search(url, deep_level=0):
    import urllib2
    from bs4 import BeautifulSoup
    print "trying to read: "+str(url)
    try:
        page = urllib2.urlopen(url)
    except:
        print "error!! ", str(url)
        return 
    soup = BeautifulSoup(page, 'html.parser')

    tags = soup.find_all('a', href=True)
    links = [tag['href'] for tag in tags] 
    results.extend(links)
    if deep_level == MAX_DEEP:
        return
    for link in links:
        search(link, deep_level+1)


