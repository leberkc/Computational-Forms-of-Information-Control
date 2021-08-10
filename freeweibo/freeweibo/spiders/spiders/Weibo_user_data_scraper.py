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

	name = "weibouser"
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
		self.curr.execute("""SELECT t1.weibo_id_user 
			FROM FreeWeiboPosts t1 
			LEFT JOIN Weibo_User_data t2 ON t1.weibo_id_user = t2.weibo_user_id 
			WHERE t2.weibo_user_id IS NULL AND t1.weibo_id_user IS NOT NULL """)
		users = self.curr.fetchall()

		for user in users:
			term = user
			yield scrapy.Request(
				f'https://m.weibo.cn/api/container/getIndex?type=uid&value={term[0]}',
				callback = self.parse_userinfo)

	def parse_userinfo(self, response):

		items = WeiboUserItem()
		jsonresponse = json.loads(response.body)
		data = jsonresponse["data"]["userInfo"]

		screen_name = data['screen_name']
		weibo_user_id = data['id']
		profile_url = data['profile_url']
		gender = data['gender']
		followers_count = data['followers_count']
		follow_count = data['follow_count']
		timestamp = datetime.datetime.now()

		items['screename'] = screen_name
		items['weibo_user_id'] = weibo_user_id
		items['profile_url'] = profile_url
		items['gender'] = gender
		items['followers_count'] = followers_count
		items['follow_count'] = follow_count
		items['timestamp'] = timestamp
		
		yield items

