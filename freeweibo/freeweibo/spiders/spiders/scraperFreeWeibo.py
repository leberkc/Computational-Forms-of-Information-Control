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
