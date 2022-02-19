# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

from DoubanGameSpider.settings import MONGODB_COLLECTION, MONGODB_DB, MONGODB_SERVER


class DoubanGameSpiderPipeline:

    def __init__(self):
        self.client = pymongo.MongoClient(MONGODB_SERVER, username='yummylee', password='qq3199619')
        self.db = self.client[MONGODB_DB]
        self.table = self.db[MONGODB_COLLECTION]

    def process_item(self, item, spider):
        self.table.insert_one(dict(item))
        print('insert one')
        return item
