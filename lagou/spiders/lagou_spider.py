# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou_spider'
    allowed_domains = ['www.lagou.com']
    # start_urls = ['http://www.lagou.com/']
    start_urls = ['https://www.lagou.com/zhaopin/webqianduan/?labelWords=label']

    def parse(self, response):
        item_list = response.xpath('//div[@id="s_position_list"]/ul/li')
        for item in item_list:
            lagou_item = LagouItem()
            # 职位名称 strip() 去掉首位空格
            lagou_item['job'] = item.xpath('./div[@class="list_item_top"]//h3/text()').extract_first().strip()
            # 城市
            lagou_item['city'] = item.xpath('./div[@class="list_item_top"]//div[@class="p_top"]//em/text()').extract_first().strip()
            # 地区
            lagou_item['area'] = item.xpath('./div[@class="list_item_top"]//span[@class="format-time"]/text()').extract_first().strip()
            # 发布时间
            lagou_item['release_time'] = item.xpath('./div[@class="list_item_top"]//span[@class="money"]/text()').extract_first().strip()
            # 薪水
            lagou_item['salary'] = item.xpath('./div[@class="list_item_top"]//div[@class="company_name"]/a/text()').extract_first().strip()
            # 工作年限
            # lagou_item['work_time'] = item.xpath('./div[@class="list_item_top"]')
            # 学历
            # education_background = scrapy.Field()
            # 公司
            lagou_item['company'] = item.xpath('./div[@class="list_item_top"]//div[@class="company_name"]/a/text()').extract_first().strip()
            # 行业
            lagou_item['industry'] = item.xpath('./div[@class="list_item_top"]//div[@class="industry"]/text()').extract_first().strip()
            yield lagou_item




