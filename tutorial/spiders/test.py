from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import YahooItem

class TestSpider(Spider):
    name = "test"
    allowed_domains = ["tw.news.yahoo.com"]
    start_urls = [
        "http://tw.news.yahoo.com/%E6%B4%AA%E4%BB%B2%E4%B8%98%E6%A1%88-10%E8%BB%8D%E5%A3%AB%E5%AE%98%E7%A7%BB%E6%AA%A2%E5%81%B5%E8%BE%A6-070113471.html",
    ]

    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        
        item = YahooItem()
        sel = Selector(response)
                
        title = sel.xpath('//h1[@class="headline"]/text()').extract()
        body = u'\n'.join(
            u''.join(p.xpath('.//text()').extract()) for p in sel.xpath('//div[@id="mediaarticlebody"]/div[@class="bd"]'))

        item['url'] = response.url

        item['title'] = title[0]
        item['body'] = body
        
        yield item