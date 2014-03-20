from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import YahooItem

class YahooSpider(CrawlSpider):
    name = "yahoo"
    allowed_domains = ["tw.news.yahoo.com"]
    start_urls = [
        "http://tw.news.yahoo.com/"
    ]
    rules = (
        # specific for golem.de -- remove for other sites
        #Rule(SgmlLinkExtractor(allow=('news\/',)), callback='parse_page', follow=True),
        Rule(SgmlLinkExtractor(allow=('.html')), callback='parse', follow=True),
    )
    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)


        item = YahooItem()
        #item['id'] = sel.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['title'] = sel.xpath('//td[@id="item_name"]/text()').extract()
        item['body'] = sel.xpath('//td[@id="item_description"]/text()').extract()


        #'''
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
        #'''