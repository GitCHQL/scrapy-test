'''
Created on 2017年3月10日

@author: qiao
'''
import scrapy
from scrapy.http import Request  
from testit.items import TestitItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/2515.html",
    ]
    def parse(self, response):
        urls = ('2906.html','831.html','2859.html','2515.html')
        for url in urls:  
            print (url)  
            url = "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/" + url  
            print (url)  
            yield Request(url, callback=self.dirparse,dont_filter=True)  

    def dirparse(self, response):    
        for sel in response.xpath('/html/body/div/div[2]/div/table/tbody'):
            item = TestitItem()
            item['title'] = sel.xpath('tr/td[1]/*/text()').extract()[0]
            #item['cx_info'] = sel.xpath('tr[1]/td[2]/table/tr/td/text()').extract()[0]
            item['name_ch'] = sel.xpath('//*[@id="complaint2"]/text()').extract()[0]
            item['name_en'] = sel.xpath('tr[4]/td[2]/text()').extract()[0]
            item['reg_num'] = sel.xpath('tr[5]/td[2]/text()').extract()[0]
            item['com_num'] = sel.xpath('tr[6]/td[2]/text()').extract()[0]
            item['reg_date'] = sel.xpath('tr[7]/td[2]/text()').extract()[0]
            item['cre_date'] = sel.xpath('tr[7]/td[4]/text()').extract()[0]
            #item['reg_date'] = sel.xpath('tr[9]/td[2]/text()').extract()
            item['reg_add'] = sel.xpath('tr[8]/td[2]/text()').extract()[0]
            item['off_add'] = sel.xpath('tr[9]/td[2]/text()').extract()[0]
            item['reg_cap'] = sel.xpath('tr[10]/td[2]/text()').extract()[0]
            item['real_cap'] = sel.xpath('tr[10]/td[4]/text()').extract()[0]
            item['com_type'] = sel.xpath('tr[11]/td[2]/text()').extract()[0]
            item['reg_rate'] = sel.xpath('tr[11]/td[4]/text()').extract()[0]
            item['type'] = sel.xpath('tr[12]/td[2]/text()').extract()[0]
            item['stuff_num'] = sel.xpath('tr[13]/td[2]/text()').extract()[0]
            item['website'] = sel.xpath('tr[13]/td[4]/a/text()').extract()[0]
            item['ismember'] = sel.xpath('tr[15]/td[2]/text()').extract()[0]
            if item['ismember']=='是':
                item['law_state'] = sel.xpath('tr[18]/td[2]/text()').extract()[0]
                item['owner'] = sel.xpath('tr[20]/td[2]/text()').extract()[0]
                item['isoffice'] = sel.xpath('tr[21]/td[2]/text()').extract()
                item['last_update'] = sel.xpath('tr[28]/td[2]/text()').extract()
                #item['sp_tips'] = sel.xpath('//*[@id="specialInfos"]/text()').extract()[0]
            else :
                item['law_state'] = sel.xpath('tr[17]/td[2]/text()').extract()[0]
                item['owner'] = sel.xpath('tr[19]/td[2]/text()').extract()[0]
                item['isoffice'] = sel.xpath('tr[20]/td[2]/text()').extract()
                item['last_update'] = sel.xpath('tr[27]/td[2]/text()').extract()
                #item['sp_tips'] = sel.xpath('//*[@id="specialInfos"]/text()').extract()[0]
            #item['reg_date'] = sel.xpath('tr[18]/td[2]/text()').extract()
            #item['link'] = sel.xpath('tr/td[2]/*/text()').extract()
            #item['desc'] = sel.css('*::text').extract()
            yield item
                    #获得下一篇文章的url  
            

  
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
            #f.write(response.xpath('//*').extract())