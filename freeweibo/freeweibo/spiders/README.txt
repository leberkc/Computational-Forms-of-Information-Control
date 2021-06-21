
response.xpath("//div[@id='right']/ol/li/a/text()").extract() //xpath for the ol of the hotsearch

response.xpath("//div[@id='right']/ol/li/a").extract() // get the links

response.xpath("//div[@class='message censored-1 deleted-0']").extract() // for one post


https://docs.scrapy.org/en/latest/intro/tutorial.html //Scrapy Documentation Page

https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3

https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python

https://coderslegacy.com/python/follow-links-in-scrapy/

https://www.w3schools.com/xml/xpath_examples.asp

https://www.youtube.com/watch?v=kkWhQKtxT2I&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=13



Using Scrapy Shell to test commands:

fetch('https://freeweibo.com/en/') - fetch the desired website
view(response) - see the page fecthed 
Use xpath selectors 
response.xpath(path) - tell scrappy what data to grab