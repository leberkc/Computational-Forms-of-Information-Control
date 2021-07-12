# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeweiboItem(scrapy.Item):
    username = scrapy.Field()
    postid = scrapy.Field()
    repostscount = scrapy.Field()
    censored = scrapy.Field()
    deleted = scrapy.Field()
    contains_adult_keyword = scrapy.Field()
    contains_censored_keyword = scrapy.Field()
    time_created = scrapy.Field()
    freeweiboOGpostlink = scrapy.Field()
    content = scrapy.Field()
    hotterm = scrapy.Field()
    timestampPostscrapped = scrapy.Field()
