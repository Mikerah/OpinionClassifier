# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    """
    Scrapy Article item for storing scraped data
    """
    title = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    type = scrapy.Field()
    id = scrapy.Field()
