# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging as log
import pymongo
from itemadapter import ItemAdapter


class EndeavorPipeline:
    def process_item(self, item, spider):
        return item


class ShipItemPipeline(object):

    collection_name = 'Ship'

    def __init__(self, mongo_url):
        self.mongo_url = mongo_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client.get_default_database()
        self.collection = self.db.get_collection(self.collection_name)

    def process_item(self, item, spider):
        ship_item = ItemAdapter(item).asdict()
        name = ship_item['Name']
        key = {'Name': name}
        try:
            old = self.collection.find_one(key)
            if old:
                self.collection.update_one(key, {"$set": ship_item})
            else:
                self.collection.insert_one(ship_item)
            log.info(f'Update ship [{name}] success.')
        except Exception as e:
            log.error(f'Update ship [{name}] failed: {e}')
        return item

    def close_spider(self, spider):
        self.client.close()
