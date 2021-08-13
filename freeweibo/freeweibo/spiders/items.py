# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeweiboItem(scrapy.Item):

    username = scrapy.Field()
    weibo_id_user = scrapy.Field()
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

class WeiboUserItem(scrapy.Item):
    
    weibo_user_id = scrapy.Field()
    screename = scrapy.Field()
    profile_url = scrapy.Field()
    statuses_count = scrapy.Field()
    verified = scrapy.Field()
    verified_type = scrapy.Field()
    verified_reason = scrapy.Field()
    close_blue_v = scrapy.Field()
    u_description = scrapy.Field()
    gender = scrapy.Field()
    mbtype = scrapy.Field()
    urank = scrapy.Field()
    mbrank = scrapy.Field()
    follow_me = scrapy.Field()
    following = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    origin = scrapy.Field()
    time_scrapped = scrapy.Field()
    
class WeiboPostItem(scrapy.Item):
    
    hotterm = scrapy.Field()
    post_id = scrapy.Field()
    mid = scrapy.Field()
    created_at = scrapy.Field()
    content = scrapy.Field()
    textLength = scrapy.Field()
    source = scrapy.Field()
    favorited = scrapy.Field()
    verified_reason = scrapy.Field()
    weibo_user_id = scrapy.Field()
    screename = scrapy.Field()
    profile_url = scrapy.Field()
    statuses_count = scrapy.Field()
    verified = scrapy.Field()
    verified_type = scrapy.Field()
    verified_type_ext = scrapy.Field()
    verified_reason = scrapy.Field()
    close_blue_v = scrapy.Field()
    u_description = scrapy.Field()
    gender = scrapy.Field()
    mbtype = scrapy.Field()
    urank = scrapy.Field()
    mbrank = scrapy.Field()
    follow_me = scrapy.Field()
    following = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()
    attitudes_count = scrapy.Field()
    origin = scrapy.Field()
    time_scrapped = scrapy.Field()
    
