# coding: utf-8


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import Selector

from tutorial.items import ImageItem



class ImageSpider(CrawlSpider):
    name = 'image'
    #allowed_domains = ['https://tw.yahoo.com/']
    start_urls = ['https://tw.yahoo.com/']
    rules = (
        Rule(SgmlLinkExtractor(allow=('\/(.+)\.html'), deny_extensions = ""), callback='parse_item'),
    )
    
    def parse_item(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//img/@src').extract()
        for site in sites:
            item = ImageItem()
            import urlparse
            image_absolute_url = urlparse.urljoin(response.url, site.strip())
            item['image_urls'] = [image_absolute_url]
            items.append(item)

        
        return items