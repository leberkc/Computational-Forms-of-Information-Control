# Information Control
This project examines methods of computatitional forms of informatiion controls.
Main themes for this research include:  Internet censorship and evasion strategies and the spread of fake news online

# FreeWeibo and Weibo Scraper

A web scraper designed to collect posts that appear on FreeWeibo.com by scraping FreeWeibo's Real-time hot search terms and  collecting all posts that contain that term(https://freeweibo.com/get-from-cache.php?q={term}). 

The scraper is also designed for Weibo's topic timeline (https://s.weibo.com/weibo/{term[0]}&Refer=STopic_box). 

The scraper will use the hot search terms collected from FreeWeibo and search Weibo.com for current posts with that term in their content. The scraper will also utilize Weibo API to collect user's data (https://m.weibo.cn/statuses/show?id={post}). No Weibo login is required. 

## Dependencies
* See requirements.txt
 
## The Database

* Utilizes MySQL Database. Database created using MySQL Workbench.
* Scripts for each table are contained in folder `Database`

1. Create Databse and First Table by using script `Hot_terms.sql`
2. Run script `FreeWeiboPosts_DB_script.sql`
3. Run script `FreeWeibo_User_data.sql`
4. Run script `Weibo_HotTerm_Topic_Post.sql`
5. Run script `Weibo_user_data.sql`

## Using Scrapy

### Create Project

First thing to do will be to create a project.

```
scrapy startproject freeweibo
```

Scrapy project will have the following file structure.

```
scrapy.cfg
freeweibo/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
```
### Modify Spiders

* Spiders are classes which define how the site or group of sites will be scrapped. Here we define the behavior for crawling and parsing pages that we desire to visit. 
* Create the first spider `scraperFreeWeibo.py` in the `spiders` folder.
* This Spider will scrap FreeWeibo Real-time hot search terms and scrape the posts.

```python
#This program is scraping information from 'https://freeweibo.com/get-from-cache.php?q='. 
#This page contains more data in json format. 
#Spider will parse through each post and scrape the data. 

import scrapy
import json
import datetime
from ..items import FreeweiboItem
from scrapy import Selector


class FreeWeiboSpider(scrapy.Spider):

	name = "freeweibo"
	allowed_domains = ['freeweibo.com']
	start_urls = ['https://freeweibo.com/']

	def parse(self, response):
		
		for hotsearchterm in response.xpath(".//div[@id='right']/ol/li/a/text()"):
			term = hotsearchterm.extract()
			yield scrapy.Request(
				f'https://freeweibo.com/get-from-cache.php?q={term}',
				callback = self.parse_hotsearchterm
				)

	def parse_hotsearchterm(self, response):

		items = FreeweiboItem()
		raw_json = response.body
		jsonresponse = json.loads(response.body)
		data = jsonresponse["messages"]

		for i in data.keys():
			user_name = data[i]['user_name']
			weibo_user_id = data[i]['user_id']
			post_id = data[i]['id']
			created = data[i]['created_at']
			reposts_count = data[i]['reposts_count']
			censored = data[i]['censored']
			deleted = data[i]['deleted']
			contains_adult_keyword = data[i]['contains_adult_keyword']
			contains_censored_keyword = data[i]['contains_censored_keyword']
			time_created = data[i]['created_at_raw']
			text = data[i]['text']
			timestamp = datetime.datetime.now()

			items['username'] = user_name
			items['weibo_user_id'] = weibo_user_id
			items['postid'] = post_id
			items['repostscount'] = reposts_count
			items['censored'] = censored
			items['deleted'] = deleted
			items['contains_adult_keyword'] = contains_adult_keyword
			items['contains_censored_keyword'] = contains_censored_keyword
			items['time_created'] = time_created
			items['freeweiboOGpostlink'] = Selector(text=created).xpath(".//a/@href").get()
			items['content'] = Selector(text=text).xpath("normalize-space()").get()
			items['hotterm'] = Selector(text=text).xpath(".//span/text()").get()
			items['timestampPostscrapped'] = timestamp
			
			yield items
```
* Create the second spider `weibo_user_data_scraper.py` in the `spiders` folder.
* This spider calls Weibo API using the users id from freeweibo to collect users data. 
```python
# weibo_user_data_scraper.py

#This program is scraping information from 'https://m.weibo.cn/api/container/getIndex?type=uid&value={term}'. 
#This page contains more data in json format. 
#Spider will parse through each post and scrape the data. 

import scrapy
import json
import datetime
from ..items import WeiboUserItem
from scrapy import Selector
import mysql.connector


class FreeWeiboSpider(scrapy.Spider):

	name = "freeweibouser"
	allowed_domains = ['m.weibo.cn']
	start_urls = ['https://m.weibo.cn']

	def __init__(self):
		self.create_connection()

	def create_connection(self):
		self.conn = mysql.connector.connect(
			host = 'localhost',
			user = 'admin',
			passwd = 'freeweibo2021',
			database = 'FreeWeibo'
			)
		self.curr = self.conn.cursor()

	def parse(self, response):

		# Checks for Users ID already on the Weibo User Data Table against the newly scrapped 
		# User ID on the FreeWeiboPosts Table. Those not in common are sent to the get a request 
		# response and have their information scrapped. 
		self.curr.execute("""
			SELECT t1.weibo_user_id 
			FROM FreeWeiboPosts t1 
			LEFT JOIN FreeWeibo_User_data t2 ON t1.weibo_user_id = t2.weibo_user_id 
			WHERE t2.weibo_user_id IS NULL AND t1.weibo_user_id IS NOT NULL 
			""")
		users = self.curr.fetchall()

		for user in users:
			term = user
			user_id = term[0]
			yield scrapy.Request(
				f'https://m.weibo.cn/api/container/getIndex?type=uid&value={term[0]}',
				callback = self.parse_userinfo, meta={'user_id': user_id})

	def parse_userinfo(self, response):

		items = WeiboUserItem()
		jsonresponse = json.loads(response.body)

		if jsonresponse["ok"] == 1:
			data = jsonresponse["data"]["userInfo"]

			items['weibo_user_id'] = data['id']
			items['screename'] = data['screen_name']
			items['profile_url'] = data['profile_url']
			items['statuses_count'] = data['statuses_count']
			items['verified'] = data['verified']
			items['verified_type'] = data['verified_type']
			if data.get('verified_reason') is None:
				items['verified_reason'] = 'No Verified_reason value given'
			else:
				items['verified_reason'] = data['verified_reason']	
			
			items['close_blue_v'] = data['close_blue_v']
			items['u_description'] = data['description']
			items['gender'] = data['gender']
			items['mbtype'] = data['mbtype']
			items['urank'] = data['urank']
			items['mbrank'] = data['mbrank']
			items['follow_me'] = data['follow_me']
			items['following'] = data['following']
			items['followers_count'] = data['followers_count']
			items['follow_count'] = data['follow_count']
			items['origin'] = 'FreeWeibo'
			items['active_status'] = True
			items['time_scrapped'] = datetime.datetime.now()
			yield items
		else:
			items['weibo_user_id'] = response.meta.get('user_id')
			items['active_status'] = False
			items['time_scrapped'] = datetime.datetime.now()

			yield items

```
* Create the third spider `weibo_topicSearch.py` in the `spiders` folder.
* This Spider searches Weibo's timeline using the hot term from FreeWeibo's Real-time hot search and collects the posts and users data. 
```python
#This program is scraping information from 'https://freeweibo.com/get-from-cache.php?q='. 
#This page contains more data in json format. 
#Spider will parse through each post and scrape the data. 

import scrapy
import json
import datetime
from ..items import WeiboPostItem
from scrapy import Selector
import mysql.connector


class FreeWeiboSpider(scrapy.Spider):

	name = "weiboTopicSearch"
	allowed_domains = ['s.weibo.com', 'm.weibo.cn']
	start_urls = ['https://s.weibo.com/']

	def __init__(self):
		self.create_connection()

	def create_connection(self):
		self.conn = mysql.connector.connect(
			host = 'localhost',
			user = 'admin',
			passwd = 'freeweibo2021',
			database = 'FreeWeibo'
			)
		self.curr = self.conn.cursor()

	# Starts the request page to search for each topic
	def start_requests(self):
		# Searches the hot terms from FreeWeibo to be searched on Weibo
		self.curr.execute("""
			SELECT HotTerm FROM HOTTERMS
			WHERE HotTerm IS NOT NULL
			ORDER BY last_time_scrapped DESC LIMIT 10;
				""")
		start_terms = self.curr.fetchall()

		for term in start_terms:
			term = term
			hotterm = term[0]
			yield scrapy.Request(
				f'https://s.weibo.com/weibo/{term[0]}&Refer=STopic_box',
				callback = self.parse_mid, meta={'hotterm': hotterm})

	# Parses the page and grabs each mid - post id for each post
	# Then requests API call to get each post data
	def parse_mid(self, response):
		for mid in response.xpath(".//div [@class='card-wrap']/@mid"):
			hotterm = response.meta.get('hotterm')
			post = mid.extract()
			yield scrapy.Request( 
				f'https://m.weibo.cn/statuses/show?id={post}',
				callback = self.parse_weiboPost, meta={'hotterm': hotterm}
				)

	# Parse through API to get all desired data for each post
	def parse_weiboPost(self, response):

		items = WeiboPostItem()
		jsonresponse = json.loads(response.body)
		data = jsonresponse["data"]
		hotterm = response.meta.get('hotterm')

		text = data['text']
		items['hotterm'] = hotterm
		items['post_id'] = data['id']
		items['mid'] = data['mid']
		items['created_at'] = data['created_at']
		items['content'] = Selector(text=text).xpath("normalize-space()").get()
		if data.get('textLength') is None:
			items['textLength'] = 'null'
		else:
			items['textLength'] = data['textLength']
		items['source'] = data['source']
		items['favorited'] = data['favorited']
		items['weibo_user_id'] = data['user']['id']
		items['screename'] = data['user']['screen_name']
		items['profile_url'] = data['user']['profile_url']
		items['statuses_count'] = data['user']['statuses_count']
		items['verified'] = data['user']['verified']
		items['verified_type'] = data['user']['verified_type']
		if data.get('verified_reason') is None:
			items['verified_reason'] = 'N/A'
		else:
			items['verified_reason'] = data['verified_reason']	
		items['close_blue_v'] = data['user']['close_blue_v']
		items['u_description'] = data['user']['description']
		items['gender'] = data['user']['gender']
		items['mbtype'] = data['user']['mbtype']
		items['urank'] = data['user']['urank']
		items['mbrank'] = data['user']['mbrank']
		items['follow_me'] = data['user']['follow_me']
		items['following'] = data['user']['following']
		items['followers_count'] = data['user']['followers_count']
		items['follow_count'] = data['user']['follow_count']
		items['reposts_count'] = data['reposts_count']
		items['comments_count'] = data['comments_count']
		items['attitudes_count'] = data['attitudes_count']
		items['origin'] = 'Weibo'
		items['time_scrapped'] = datetime.datetime.now()
		
		yield items
```
### Modify Items
* Spiders will return extraced data as items. 
* Modify `items.py`.
```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeweiboItem(scrapy.Item):

    username = scrapy.Field()
    weibo_user_id = scrapy.Field()
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
    active_status = scrapy.Field()
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


class CombinedItem(scrapy.Item):
    username = scrapy.Field()
    weibo_user_id = scrapy.Field()
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
    active_status = scrapy.Field()
    time_scrapped = scrapy.Field()
    
```

### Modify Pipelines
* After the items have been scraped by the spiders, it will be sent to the Item Pipeline which processes using several components that are executed sequentially. 
* Modify `pipelines.py`.
```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class FreeweiboPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'admin',
            passwd = 'freeweibo2021',
            database = 'FreeWeibo'
            )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        
        if spider.name == 'freeweibo':

            values = [item['hotterm']]

            self.curr.execute("""
            SELECT HotTerm
            FROM HOTTERMS  
            WHERE HotTerm = (%s)
            """, values)

            result = self.curr.fetchall()

            if self.curr.rowcount >= 1:
                self.store_update_hotterms_db(item)
                self.store_post_db(item)
                return item
            else:
                self.store_hotterms_db(item)
                self.store_post_db(item)
                return item

        if spider.name == 'freeweibouser':

            if item['active_status'] is False:
                self.store_freeweibo_inactive_user_db(item)
                return item
            else:
                self.store_freeweibo_user_db(item)
                return item

        if spider.name == 'weiboTopicSearch':
            self.store_weibo_post_db(item)
            self.store_weibo_user_db(item)
            return item

        if spider.name == 'oneprocessfreeweibo':

            values = [item['hotterm']]

            self.curr.execute("""
            SELECT HotTerm
            FROM HOTTERMS  
            WHERE HotTerm = (%s)
            """, values)

            result = self.curr.fetchall()

            if self.curr.rowcount >= 1:
                self.store_update_hotterms_db(item)
                self.store_post_db(item)
                if item['active_status'] is False:
                    self.store_freeweibo_inactive_user_db(item)
                else:
                    self.store_freeweibo_user_db(item)
                return item
            else:
                self.store_hotterms_db(item)
                self.store_post_db(item)
                if item['active_status'] is False:
                    self.store_freeweibo_inactive_user_db(item)
                else:
                    self.store_freeweibo_user_db(item)
                return item

    def store_post_db(self, item):
        post_values =[
            item['username'], 
            item['weibo_user_id'],
            item['postid'], 
            item['repostscount'], 
            item['censored'], 
            item['deleted'], 
            item['contains_adult_keyword'], 
            item['contains_censored_keyword'], 
            item['time_created'], 
            item['freeweiboOGpostlink'], 
            item['hotterm'], 
            item['content'], 
            item['timestampPostscrapped']
        ]

        self.curr.execute(
            """INSERT INTO FreeWeiboPosts 
            VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",post_values
            )
        self.conn.commit()

    def store_hotterms_db(self, item):
        post_values =[
            item['hotterm'], 
            item['timestampPostscrapped'],
            item['timestampPostscrapped']
        ]

        self.curr.execute(
            "INSERT INTO HOTTERMS VALUES (NULL,%s,%s,%s)",post_values
            )
        self.conn.commit()

    def store_update_hotterms_db(self, item):

        values =[
            item['timestampPostscrapped'],
            item['hotterm']
        ]

        self.curr.execute(
            """UPDATE HOTTERMS 
            SET last_time_scrapped = (%s)
            WHERE HotTerm = (%s)
            """, values)

        self.conn.commit()

    def store_freeweibo_user_db(self, item):
        user_values =[
            item['weibo_user_id'],
            item['screename'],
            item['profile_url'], 
            item['statuses_count'],  
            item['verified'],
            item['verified_type'],
            item['verified_reason'],
            item['close_blue_v'], 
            item['u_description'], 
            item['gender'], 
            item['mbtype'],
            item['urank'], 
            item['mbrank'], 
            item['follow_me'],
            item['following'],
            item['followers_count'],
            item['follow_count'],
            item['origin'],
            item['active_status'],
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO FreeWeibo_User_data 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ,user_values)
        self.conn.commit()

    def store_freeweibo_inactive_user_db(self, item):
        user_values =[
            item['weibo_user_id'],
            item['active_status'],
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO FreeWeibo_User_data (weibo_user_id,active_status,time_scrapped) 
            VALUES (%s,%s,%s)"""
            ,user_values)
        self.conn.commit()

    def store_weibo_post_db(self, item):
        post_values =[
            item['hotterm'],
            item['post_id'],
            item['mid'],
            item['created_at'], 
            item['content'],
            item['textLength'],  
            item['source'],
            item['favorited'],
            item['weibo_user_id'],
            item['reposts_count'],
            item['comments_count'], 
            item['attitudes_count'], 
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO Weibo_HotTerm_Topic_Post 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ,post_values)
        self.conn.commit()

    def store_weibo_user_db(self, item):
        user_values =[
            item['weibo_user_id'],
            item['screename'],
            item['profile_url'], 
            item['statuses_count'],  
            item['verified'],
            item['verified_type'],
            item['verified_reason'],
            item['close_blue_v'], 
            item['u_description'], 
            item['gender'], 
            item['mbtype'],
            item['urank'], 
            item['mbrank'], 
            item['follow_me'],
            item['following'],
            item['followers_count'],
            item['follow_count'],
            item['origin'],
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO Weibo_User_data 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ,user_values)
        self.conn.commit()
```
### Modify Settings
* The Scrapy settings allows you to customize the behavior of all Scrapy components, extensions, pipelnes and spiders. 
* Modify `settings.py`.
```pyton
# Scrapy settings for freeweibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'freeweibo'

SPIDER_MODULES = ['freeweibo.spiders']
NEWSPIDER_MODULE = 'freeweibo.spiders'
FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'freeweibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'freeweibo.middlewares.FreeweiboSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'freeweibo.middlewares.FreeweiboDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'freeweibo.pipelines.FreeweiboPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```
## Run Scrapy Spiders
* First go to project directory.
```
cd freeweibo
```
* Run the first spider
```
scrapy crawl freeweibo
```
* Run the second spider
```
scrapy crawl freeweibouser
```
* Run the third spider
```
scrapy crawl weiboTopicSearch
```
* Check database to see all the information scrapped saved in the database. 

## Using Bash Script
* Scrapy can only run one spider at a time. 
* To continually use the spiders to collect data using a cron job, it can be done by using the following bash script.
```bash
#!/bin/bash

cd /myfolder/freeweibo
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl freeweibo
wait
scrapy crawl weiboTopicSearch
wait
scrapy crawl freeweibouser
```
* Location of where scrapy is installed can be found by the following command
```
where scrapy
```
* Copy and paste that path to $PATH:{paste outcome here}
* Make the bash script executable
```
chmod +x filename.sh
```
* Run script
```
./filename.sh
```
