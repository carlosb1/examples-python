import scrapy


class TorrentSpyder(scrapy.Spider):
    name = 'torrent'
    start_urls = ['https://proxyspotting.in/top/205']

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse);
    
    def parse(self,response):
        for page_url in response.xpath('//div[contains(@class,"detName")]'):
            print str(page_url.extract())    
