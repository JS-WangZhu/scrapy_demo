# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class MyscrapyPipeline:

    def process_item(self, item, spider):
        return item


class BaiduPipeline:
    fp = None

    def open_spider(self, spider):
        print("开始爬虫")

    def process_item(self, item, spider):
        name = item['name']
        link = item['link']
        # sava mongodb
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["baidu"]
        mycol = mydb["hotpoints"]
        mycol.insert_one({'name': name, 'link': link})
        return item

    def close_spider(self, spider):
        print("结束爬虫")
