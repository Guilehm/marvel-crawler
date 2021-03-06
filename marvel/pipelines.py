# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

from pymongo import MongoClient

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/marvelCrawler')


class MarvelPipeline(object):

    def __init__(self):
        self.mongo_client = MongoClient(MONGODB_URI)
        self.db = self.mongo_client.marvelCrawler

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.insert_one(dict(item))
        return item
