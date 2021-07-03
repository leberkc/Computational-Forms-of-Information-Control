# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeweiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # username = scrapy.Field()
    # usernamelink = scrapy.Field()
    # hashtags = scrapy.Field()
    # hashtagslinks = scrapy.Field()
    # content = scrapy.Field()
    # date = scrapy.Field()
    # censored = scrapy.Field()
    # now = scrapy.Field()
    #pass
    
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
    hashtags = scrapy.Field()
    hashtagsurls = scrapy.Field()
    timestampscrapped = scrapy.Field()
