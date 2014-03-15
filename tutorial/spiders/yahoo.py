from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import YahooItem

class YahooSpider(Spider):
    name = "yahoo"
    allowed_domains = ["tw.news.yahoo.com"]
    start_urls = [
        "http://tw.news.yahoo.com/%E8%97%8F%E6%B5%B7%E6%B4%9B%E5%9B%A0%E9%97%96%E9%97%9C-%E7%98%B8%E8%85%BF%E7%94%B7%E5%88%A4%E5%88%91%E5%AE%9A%E8%AE%9E-040807265.html"
    ]

    def parse(self, response):
        item = YahooItem()
        sel = Selector(response)
                    
        title = sel.xpath('//h1[@class="headline"]/text()').extract()
        body = sel.xpath('//div[@class="bd"]/text()').extract()
        if 0 < len(title):
            item['title'] = title[0]
            item['body'] = body[0]
        else:
            item['title'] = ''
            item['body'] = ''
        yield item