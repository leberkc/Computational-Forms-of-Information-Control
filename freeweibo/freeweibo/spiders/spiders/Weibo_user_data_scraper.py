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

