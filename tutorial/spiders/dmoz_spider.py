from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader 


from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):  
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items = []
        for site in sites:
            l = ItemLoader(item=DmozItem(), response=response)  
            l.add_xpath('title', 'a/text()')  
            l.add_xpath('link', 'a/@href')  
            l.add_xpath('desc', 'text()')  
            items.append(l.load_item())


        return items

 
