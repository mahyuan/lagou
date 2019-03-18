# -*- coding: UTF-8 -*-

from scrapy import cmdline

# cmdline.execute('scrapy crawl lagou_spider FEED_EXPORT_ENCODING=utf-8'.split())
# cmdline.execute('scrapy crawl lagou_spider'.split())
# cmdline.execute(['scrapy', 'crawl', 'lagou_spider', 'FEED_EXPORT_ENCODING=utf-8'])
cmdline.execute(['scrapy', 'crawl', 'lagou_spider', '-o', 'text.json', '-s', 'FEED_EXPORT_ENCODING=utf-8 bom'])
