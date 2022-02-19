# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanGameItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    platforms = scrapy.Field()
    genres = scrapy.Field()
    rating = scrapy.Field()
    douban_url = scrapy.Field()
    rating_nums = scrapy.Field()
    douban_id = scrapy.Field()
    cover = scrapy.Field()
    pass
