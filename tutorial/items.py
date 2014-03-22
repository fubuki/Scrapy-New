# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class NewsItem(Item):
    title = Field()
    body = Field()
    time = Field()
    
class YahooItem(Item):
    title = Field()
    body = Field()
    url = Field()