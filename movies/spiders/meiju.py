# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'      # 爬虫名。一个项目下可能有多个爬虫，并且每个爬虫有优先级、并发等设置。scrapy crawl [spider_name]
    allowed_domains = ['www.meijutt.com']       # 为了防止爬虫项目自动爬取到其他网站。设置限制，每一次请求前都会检查请求的网址是否属于这个域名，是的话才允许请求。注意：爬取日志爬取网址后响应总为None，检查allowed domain 书写是否正确。值是一级域名。
    start_urls = ['https://www.meijutt.com/new100.html']    # 第一个请求的url，所有请求的入口。得到的response返回给self.parse(self,response)

    def parse(self, response):
        # print(response.text)
        # 非框架写法 dom = lxml.etree.HTML(response.text);dom.xpath('')
        resp = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for li in resp:
            titles = li.xpath('//h5/a/text()').extract   # 表示在子标签的基础上继续解析
            item = MoviesItem()
            item.name = titles      # item['name'] = name
            yield item          # yield 相当于同步脚本方法中的return

            

