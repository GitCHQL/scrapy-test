# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title =scrapy.Field()
    link  =scrapy.Field()
    desc =scrapy.Field()
    cx_info =scrapy.Field()
    name_ch =scrapy.Field()
    name_en =scrapy.Field()
    reg_num =scrapy.Field()
    com_num =scrapy.Field()
    reg_date =scrapy.Field()
    cre_date =scrapy.Field()
    reg_add =scrapy.Field()
    off_add =scrapy.Field()
    reg_cap =scrapy.Field()
    real_cap =scrapy.Field()
    com_type =scrapy.Field()
    reg_rate =scrapy.Field()
    type =scrapy.Field()
    stuff_num =scrapy.Field()
    website =scrapy.Field()
    ismember =scrapy.Field()
    law_state =scrapy.Field()
    owner =scrapy.Field()
    isoffice =scrapy.Field()
    last_update =scrapy.Field()
    sp_tips =scrapy.Field()
    
    
    pass
