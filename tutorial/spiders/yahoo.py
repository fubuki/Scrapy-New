
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from tutorial.items import YahooItem

class YahooSpider(CrawlSpider):
    name = "yahoo"
    allowed_domains = ["tw.news.yahoo.com"]
    start_urls = [
        "http://tw.news.yahoo.com"
    ]
    rules = (
        
        Rule(SgmlLinkExtractor(allow=('\/(.+)\.html'), deny_extensions = ""), callback='parse_news'),
    )


    def parse_news(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        
        item = YahooItem()
        sel = Selector(response)
                
        title = sel.xpath('//h1[@class="headline"]/text()').extract()
        body = u'\n'.join(
            u''.join(p.xpath('.//text()').extract()) for p in sel.xpath('//div[@id="mediaarticlebody"]/div[@class="bd"]'))

        item['url'] = response.url
        if 0 < len(title):
            item['title'] = title[0]
            item['body'] = body[0]
        else:
            item['title'] = ''
            item['body'] = ''
        yield item
        