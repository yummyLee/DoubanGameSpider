import scrapy
import json
from scrapy.selector import Selector

from DoubanGameSpider.items import DoubanGameItem


class DoubanGameSpider(scrapy.Spider):
    name = 'game_spider'

    def start_requests(self):
        url_pre = 'https://www.douban.com/j/ilmen/game/search?genres=&platforms=&q=&sort=rating&more='
        urls = []
        for i in range(1, 2):
            urls.append(url_pre + str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('=')[-1]
        # filename = 'douban_game-%s.json' % page
        # print(response.xpath('//pre/text()').get())
        douban_json = json.loads(response.xpath('//pre/text()').get())
        item = DoubanGameItem()
        for douban_json_item in douban_json.get('games'):
            item['name'] = douban_json_item.get('title')
            item['platforms'] = douban_json_item.get('platforms').split(' / ')
            item['genres'] = douban_json_item.get('genres').split(' / ')
            item['rating'] = float(douban_json_item.get('rating'))
            item['douban_url'] = douban_json_item.get('url')
            item['rating_nums'] = douban_json_item.get('n_ratings')
            item['douban_id'] = douban_json_item.get('id')
            item['cover'] = douban_json_item.get('cover')
            yield item

        # with open(filename, 'wb') as f:
        #     f.write(response.xpath('//pre/text()').get())
        # self.log('Saved File %s' % filename)
