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
				callback = self.parse_hotsearchterm, meta={'hotterm': term}
				)

	def parse_hotsearchterm(self, response):

		items = FreeweiboItem()
		raw_json = response.body
		hotterm = response.meta.get('hotterm')
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
			#items['hotterm'] = Selector(text=text).xpath(".//span/text()").get()
			items['hotterm'] = hotterm
			items['timestampPostscrapped'] = timestamp
			
			yield items
