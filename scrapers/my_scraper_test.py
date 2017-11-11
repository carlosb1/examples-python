from my_scraper import ProxyProvider, FakeParser, FakeDownloader, Scrapper, LinkParser, DownloaderURLLIB2
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

