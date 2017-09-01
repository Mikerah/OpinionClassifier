# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import hashlib
from scrapy.conf import settings
from scrapy.exceptions import DropItem
        
class MongoPipeline(object):
    """
    Pipeline for storing article items in a mongoDB database
    """
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.ids_seen = set()
        
    def process_item(self, item, spider):
        # Clean data
        # Cleaning author data
        if 'author' not in item:
            item['author'] = 'No Author'
        elif len(item['author']) > 1:
            item['author'] = ','.join(item['author'])
        else:
            item['author'] = item['author'][0]
            
        # Cleaning title data
        item['title'] = item['title'][0]
        
        # Cleaning url data
        item['url'] = item['url'][0]
        
        # Cleaning article text data
        item['text'] = ''.join(item['text'])
        
        # Cleaning type data
        item['type'] = item['type'][0]
        
        # Create unique identifier for article 
        item['id'] = hashlib.sha256(item['url'].encode()).hexdigest()
        
        # Check if there is a duplicate article
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate Article")
        else:
            self.ids_seen.add(item['id'])
            self.collection.insert(dict(item))
            return item
        
        
