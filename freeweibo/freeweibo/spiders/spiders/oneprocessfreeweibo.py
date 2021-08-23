#This program is scraping information from 'https://freeweibo.com/get-from-cache.php?q='. 
#This page contains more data in json format. 
#Spider will parse through each post and scrape the data. 

import scrapy
import json
import datetime
from ..items import CombinedItem
from scrapy import Selector


class FreeWeiboSpider(scrapy.Spider):

	name = "oneprocessfreeweibo"
	allowed_domains = ['freeweibo.com','m.weibo.cn']
	start_urls = ['https://freeweibo.com/']

	def parse(self, response):
		
		for hotsearchterm in response.xpath(".//div[@id='right']/ol/li/a/text()"):
			term = hotsearchterm.extract()
			yield scrapy.Request(
				f'https://freeweibo.com/get-from-cache.php?q={term}',
				callback = self.parse_hotsearchterm
				)

	def parse_hotsearchterm(self, response):

		items = CombinedItem()
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

			yield scrapy.Request(
				f'https://m.weibo.cn/api/container/getIndex?type=uid&value={weibo_user_id}',
				callback = self.parse_userinfo, meta={'item': items})


	def parse_userinfo(self, response):

		items = response.meta['item']

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

