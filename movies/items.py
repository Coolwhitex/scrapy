# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 类似django orm中的models.py
    # item 不管什么字段都是scrapy.Field(),不区分类型
    name = scrapy.Field()
    pass
