import os
# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'


ITEM_PIPELINES = [
  #'scrapy_mongodb.MongoDBPipeline',
  'scrapy.contrib.pipeline.images.ImagesPipeline'
]

#MONGODB_URI = 'mongodb://192.168.65.141:27017'
#MONGODB_DATABASE = 'scrapy'
#MONGODB_COLLECTION = 'bbc'
#MONGODB_UNIQUE_KEY = 'title'

DEPTH_LIMIT = 3

DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_STORE = os.path.join(DIR, '..', 'images')