# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class LuoyangspiderSpider(scrapy.Spider):
    name = 'luoyangSpider'
    allowed_domains = ['tianqi.com']
    #start_urls = ['http://www.tianqi.com/luoyang',]
    citys = ['luoyang','kaifeng','shunyi','hangzhou','handan','qingdao']
    start_urls = []
    for city in citys:
        start_urls.append('https://www.tianqi.com/' + city)


    def parse(self, response):
        subSelector = response.xpath('//div[@class = "left"]')
        #subSelector = response.xpath('//div[@class = "left"]')
        items = []
        for sub in subSelector:
            item = WeatherItem()
            '''这一段注释掉，因为原样例需要拼合为 城市今日天气，但现在只有城市名称
            cityDates = ''
            for cityDate in sub.xpath('.//dd[1]/h2/text()').extract():
                cityDates += cityDate
            item['cityDate'] = cityDates'''
            try:
                item['cityDate'] = sub.xpath('.//dd[1]/h2/text()').extract()[0]
                item['week'] = sub.xpath('.//dd[2]/text()').extract()[0]
                item['img'] = sub.xpath('.//dd[3]/i/img/@src').extract()[0]
                # 执行拼合 得到 "阴" + "21-28度"  这样的结果
                temps = ''
                for temp in sub.xpath('.//dd[3]/span//text()').extract():
                    temps += temp
                item['temperature'] = temps
                # weather没了，还是取另一个温度吧
                weathers = ''
                for weather in sub.xpath('.//dd[3]/p//text()').extract():
                    weathers += weather
                item['weather'] = weathers
                winds = ''
                for wind in sub.xpath('.//dd[4]//text()').extract():
                     winds += wind
                item['wind'] = winds
                items.append(item)
            except IndexError:
                pass
        return items

