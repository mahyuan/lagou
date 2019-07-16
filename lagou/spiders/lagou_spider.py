# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou_spider' # 爬虫的名字，唯一性
    allowed_domains = ['www.lagou.com']
    # start_urls = ['https://www.lagou.com/zhaopin/webqianduan/1/?filterOption=3']
    # start_urls = ['https://www.lagou.com/zhaopin/reactnative?filterOption=3']
    start_urls = ['https://www.lagou.com/jobs/list_react%20native/1']

    def parse(self, response):
        item_list = response.xpath('//div[@id="s_position_list"]/ul/li')
        for item in item_list:
            lagou_item = LagouItem()
            # 职位名称 strip() 去掉首位空格
            lagou_item['job'] = item.xpath('./div[@class="list_item_top"]//h3/text()').extract_first().strip()
            location = item.xpath('./div[@class="list_item_top"]//div[@class="p_top"]//em/text()').extract_first().strip()
            if '·' in location:
                l_location = location.split('·')
                # 城市
                lagou_item['city'] = l_location[0].strip()
                lagou_item['area'] = l_location[1].strip() if len(location) > 0 else ''
            else:
                lagou_item['city'] = location[0].strip()

            # 发布时间
            lagou_item['release_time'] = item.xpath('./div[@class="list_item_top"]//span[@class="format-time"]/text()').extract_first().strip()
            # 薪水
            lagou_item['salary'] = item.xpath('./div[@class="list_item_top"]//span[@class="money"]/text()').extract_first().strip()

            requirements = "".join(item.xpath('./div[@class="list_item_top"]//div[@class="p_bot"]/div/text()').extract()).strip().split('/')
            if isinstance(requirements, list):
                # 工作年限
                lagou_item['experience'] = requirements[0].strip()
                # 学历
                lagou_item['education'] = requirements[1].strip()
            # 公司
            lagou_item['company'] = item.xpath('./div[@class="list_item_top"]//div[@class="company_name"]/a/text()').extract_first().strip()

            industry_list = item.xpath('./div[@class="list_item_top"]//div[@class="industry"]/text()').extract_first().strip().split('/')
            if isinstance(industry_list, list):
                # 行业
                lagou_item['industry'] = industry_list[0].strip()
                # 融资
                lagou_item['financing'] = industry_list[1].strip()
                # 贵司规模
                lagou_item['company_size'] = industry_list[2].strip()
            yield lagou_item

        next_link = response.xpath('//div[@class="pager_container"]/a[contains(@class,"pager_is_current")]/following-sibling::a[1]/@href').extract_first()
        if next_link:
            yield scrapy.Request(next_link, callback=self.parse)


