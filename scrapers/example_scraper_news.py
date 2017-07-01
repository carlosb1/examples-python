
import urllib2
import string 

import shutil,os
class DownloaderURLLIB2():
    name = 'test.html'
    repositories_download="repositories.txt"
    black_list = []
    def set_name(self,name):
        self.name = name
    def get(self,url):
        import urllib2
        response = urllib2.urlopen(url)
        return response.read()
    def download(self,url,dir_down="downloaded/"):
        proxy = ProxyProvider(self.repositories_download)
         
        #shutil.rmtree(dir_down,ignore_errors=True)
        if not os.path.exists(dir_down): 
            os.makedirs(dir_down)

        num_proxies = len(proxy.proxies)
        tr = 0
        while tr < 5:
            candidate = proxy.proxies[randint(0,num_proxies-1)]
            try:
                if url in self.black_list:
                    return
                print "connecting url: ",url
                new_url=''.join(e for e in url if e.isalnum())
                print "using proxy: ",str(candidate[1][0])+":"+str(candidate[1][1])
                proxy_url = str(candidate[1][0])+":"+str(candidate[1][1])

                proxy_support = urllib2.ProxyHandler({"http":'http://'+proxy_url})
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)
                info = urllib2.urlopen(url,timeout=10)
                with open(dir_down+"/"+new_url,"w") as fil:
                    fil.seek(0)
                    fil.write(info.read())
                    fil.close()
                print "trying to save information"
                return
            except Exception as e:
                print "It was not possible download info: ", e
                self.black_list.append(url)

            tr+=1
        
        self.black_list.append(url)


import urllib
from random import randint

class FakeDownloader(DownloaderURLLIB2):
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
            print str(text.encode('utf8'))
            text = self.add_prefix(text,url)
            if self.is_correct_link(text):
                if not text in self.links:
                    self.links.append(text)
        return parsedInfo

    def add_prefix(self,text,url):
        if text.startswith('//'):
            return "http:"+text
        if text.startswith('/'):
            text=url+text
            return text
        return text
    def is_correct_link(self,text):
        return text.startswith('http')

class FakeParser:
    links = []
    def execute(self,url,data):
        return ""

import time
import random
class Scrapper:
    def __init__(self,downloader, parser):
        self.downloader = downloader
        self.parser = parser
        
    def run(self,url):
        info = self.downloader.get(url)
        self.parser.execute(url,info)
        return info

    def download_links(self):
       for link in self.parser.links:
           print "trying to download this link: ",link
           time.sleep(random.randint(0,1000) / 100)
           self.downloader.download(link,"downloader/")


import os
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

#TODO not a correct test!!
    def test_should_start_http_download_links(self):
        downloader = FakeDownloader()
        parser = LinkParser()
        scrapper = Scrapper(downloader,parser)
        #TODO check input
        scrapper.run('http://elpais.com')

        scrapper.download_links()

