# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道：数据清洗、去重。
# 持久化： 写入数据库。写txt，csv

# scrapy框架将爬取spider模块和处理层pipline 分离开，使得程序更容易扩展。
# spider yield生成的item会交给pipline处理。如果爬取速度跟处理速度不一致的话，scrapy框架会自动调度。
# spider yield 相当于生产消费模型中的生产者，pipline 相当于消费者。


class MoviesPipeline(object):
    def process_item(self, item, spider):
        with open('movie.txt', 'a', encoding='utf-8') as f:
            f.write(str(item['name']) + '\n')
        return item
