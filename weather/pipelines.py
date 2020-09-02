# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path
import urllib.request

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        '''
        fileName = today + '.json'
        with codecs.open(fileName,'a',encoding = 'utf8') as fp:
            line = json.dumps(dict(item),ensure_ascii = False) + '\n'
            fp.write(line)'''

        fileName = today + '.txt'
        with open(fileName, mode='a', encoding='utf-8') as fp:
            fp.write(item['cityDate'] + '\t')
            fp.write(item['week'] + '\t')
            imgName = os.path.basename(item['img'])
            fp.write(imgName + '\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName, 'wb') as fp:
                    response = urllib.request.urlopen(item['img'])
                    fp.write(response.read())
            fp.write(item['temperature'] + '\t')
            fp.write(item['weather'] + '\t')
            fp.write(item['wind'] + '\n')
            time.sleep(2)
            #fp.close()
        return item
        #fp.close()