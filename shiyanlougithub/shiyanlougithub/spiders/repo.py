# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import RepoItem

class RepoSpider(scrapy.Spider):
    name = 'repo'

    @property
    def start_urls(self):
        url_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'     
        return (url_tmp1.format(i) for i in range(1,5))

    def parse(self, response):
        for course in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield RepoItem({
                
                    'name':course.xpath('div[1]/h3/a/text()').re_first('\n\s*(.+)'),
                    'update_time': course.xpath('div[3]/relative-time/@datetime').extract_first()
               })  
        
