from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import YahooItem

class DebugSpider(Spider):
    name = 'debug'
    start_urls = (
        'http://www.google.com.tw',
        'http://tw.yahoo.com',
        )

    def parse(self, response):
        # collect `item_urls`
        for item_url in item_urls:
            yield Request(url=item_url, callback=self.parse_item)

    def parse_item(self, response):
        item = MyItem()
        # populate `item` fields
        yield Request(url=item_details_url, meta={'item': item},
            callback=self.parse_details)

    def parse_details(self, response):
        item = response.meta['item']
        # populate more `item` fields
        return item