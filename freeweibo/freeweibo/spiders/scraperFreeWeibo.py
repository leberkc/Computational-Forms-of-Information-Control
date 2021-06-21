import scrapy
from ..items import FreeweiboItem


class FreeWeiboSpider(scrapy.Spider):
	#
	name = "freeweibo"
	allowed_domains = ['freeweibo.com']
	start_urls = ['https://freeweibo.com/en/weibo']

	def parse(self, response):

		items = FreeweiboItem()
		banned_posts = response.xpath(".//div[@class='message censored-1 deleted-0']")
		for post in banned_posts:
			username = post.xpath(".//div[@class='content']/a/text()")
			usernamelink = post.xpath(".//div[@class='content']/a/@href")
			hashtags = post.xpath(".//div[@class='content']/a/text()")
			hashtagslinks = post.xpath(".//div[@class='content']/a/@href")
			content = post.xpath("normalize-space(.//div[@class='content'])")
			#content = banned_posts.xpath(".//div[@class='content']/text()")
			date = 	post.xpath(".//div[@class='date']/a/text()")
			censored = post.xpath(".//span[@class='censored']/text()")
			now = datetime.now()

			items['username'] = username.extract_first()
			items['usernamelink'] = usernamelink.extract_first()
			items['hashtags'] = hashtags[1:].extract()
			items['hashtagslinks'] = hashtagslinks[1:].extract()
			items['content'] = content.extract()
			items['date'] = date.extract()
			items['censored'] = censored.extract()
			items['now'] = now
			yield items
			
		# This will follow each link contained inside the content of each post
		#for next_link in response.xpath(".//div[@class='content']/a/@href"):
		 	#yield response.follow(next_link, self.parse)
		# This will get each link in the hot search ordered list	
		#for next_term in response.xpath(".//div[@id='right']/ol/li/a"):
			#yield response.follow(next_term, self.parse)
		# This will follow view older messages
		for next_link in response.xpath(".//div[@id='load-older']/a/@href"):
			yield response.follow(next_link, self.parse)


