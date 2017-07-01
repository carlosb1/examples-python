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
    name = 'test.html'
    def set_name(self,name):
        self.name = name
    def get(self,url):
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
            text = self.add_prefix(text,url)
            if self.is_correct_link(text):
                self.links.append(text)
        return parsedInfo

    def add_prefix(self,text,url):
        if text.startswith('/'):
            text=url+text
        return text
    def is_correct_link(self,text):
        return text.startswith('http')

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

import os
import urllib
import heapq
class ProxyProvider:
    repositories = []
    proxy_names = []
    proxies = []
    def __init__(self,filename):
        self.filename = filename
        with open(filename,'r') as fil:
            self.repositories = [repository for repository in fil.readlines()]

    def load(self):
        index=0
        for repository in self.repositories:
            name_proxy = "proxy_list"+str(index)
            urllib.urlretrieve (repository,name_proxy)
            self.proxy_names.append(name_proxy)
            index+=1
        for proxy_name in self.proxy_names:
            with open(proxy_name,'r') as fil:
                for possible_address in fil.readlines():
                    address=possible_address.split(':')
                    if len(address) == 2:
                        try:
                            heapq.heappush(self.proxies,(1,[str(address[0]),int(address[1])]))
                        except:
                            print "It was not possible to save proxy address "+str(address)
import unittest


class TestRepository(unittest.TestCase):
    def test_should_be_initialised_with_one_repository(self):
        proxy = ProxyProvider('repositories.txt')
        self.assertTrue(len(proxy.repositories)==1)

    def test_load_available_proxies_from_one_repository(self):
        proxy = ProxyProvider('repositories.txt')
        proxy.load()
        self.assertTrue(len(proxy.proxy_names)>0)

    def test_load_proxies_from_list_repositorues(self):
        proxy = ProxyProvider('repositories.txt')
        proxy.load()
        self.assertTrue(len(proxy.proxies)>0)

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




