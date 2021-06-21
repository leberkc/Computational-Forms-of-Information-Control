# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeweiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    usernamelink = scrapy.Field()
    hashtags = scrapy.Field()
    hashtagslinks = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    censored = scrapy.Field()
    now = scrapy.Field()
    #pass
