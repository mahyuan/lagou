# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# 从settings导入数据
from lagou.settings import mongo_host, mongo_port, mongo_db_name, mongo_collection

class LagouPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = mongo_collection
        cliect = pymongo.MongoClient(host=host, port=port)
        lagoudb = cliect[dbname]
        self.post = lagoudb[collection]

    def process_item(self, item, spider):
        # 插入数据
        data = dict(item)
        self.post.insert(data)
        # return item
