#check info
#import urllib2
#response = urllib2.urlopen('http://elpais.com')
#with open('test.html','w') as fil:
#    fil.write(response.read())


def download_url(url):
    import urllib2
    response = urllib2.urlopen(url)
    return response.read()
    

class DownloaderURLLIB2():
    import urllib2
    response = urllib2.urlopen(url)
    return response.read()

class FakeDownloader():
    name = 'test.html'
    def set_name(self,name):
        self.name = name
    def get(self,url):
        with open(self.name,'r') as fil:
            data = fil.read()
            return data
        return ""


from bs4 import BeautifulSoup

class LinkParser:
    links = []
    def execute(self,url,data):
        parsedInfo = BeautifulSoup(data,'lxml')
        for link in  parsedInfo.select('a[href]'):
            text = link.get('href')
            #move to function
            if text.startswith('/'):
                text=url+text
            if text.startswith('http'): 
                self.links.append(text)
        return parsedInfo

class FakeParser:
    links = []
    def execute(self,url,data):
        return ""


class Scrapper:
    def __init__(self,downloader, parser):
        self.downloader = downloader
        self.parser = parser
        
    def run(self,url):
        info = self.downloader.get(url)
        self.parser.execute(url,info)
        return info
        
   

import unittest

class TestScrapper(unittest.TestCase):
    def test_read_url(self):
        downloader = FakeDownloader()
        fakeParser = FakeParser()
        scrapper = Scrapper(downloader,fakeParser)
        #TODO move data
        data = scrapper.run('http://elpais.com')
        self.assertTrue(len(data)>0)


    def test_should_return_links(self):
        downloader = FakeDownloader()
        parser = LinkParser()
        scrapper = Scrapper(downloader,parser)
        #TODO check input
        scrapper.run('http://elpais.com')

        info = scrapper.parser.links
        self.assertTrue(len(info)>0) 

    def test_should_start_http_links(self):
        downloader = FakeDownloader()
        parser = LinkParser()
        scrapper = Scrapper(downloader,parser)
        #TODO check input
        scrapper.run('http://elpais.com')

        info = scrapper.parser.links
        for link in info:
            self.assertTrue(link.startswith('http')) 




