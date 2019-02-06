# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 职位名称
    job = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 地区
    area = scrapy.Field()
    # 发布时间
    release_time = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 工作年限
    work_time = scrapy.Field()
    # 学历
    education_background = scrapy.Field()
    # 公司
    company = scrapy.Field()
    # 行业
    industry = scrapy.Field()
