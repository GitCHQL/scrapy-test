# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class TestitPipeline(object):
    def process_item(self, item, spider):
        for key in item:
            item[key]=item[key].replace('\n','')
            item[key]=item[key].replace('\r','')
            item[key]=item[key].replace(' ','')
            item[key]=item[key].replace('\t','')
            item[key]=item[key].replace('\xa0','')
            item[key]=item[key].replace('&nbsp','')
        #line = json.dumps(dict(item)) + '\n'  
        #self.file.write(line.decode("unicode_escape"))  
        return item
    def __init__(self):  
        self.file = codecs.open('CSDNBlog_data.json', mode='wb', encoding='utf-8')  