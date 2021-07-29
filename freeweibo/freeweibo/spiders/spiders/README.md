About Scrapy

  Scrapy is a fast high-level screen scraping and web crawling framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

    http://www.scrapy.org

Using the scrapy shell

  Use the Scrapy shell to load a page and experiment with XPath queries. Once you're happy with the query that extracts interesting data you can use it in your spider. 

  To enter the shell, use scrapy shell http://example.com (where you replace the URL with your own). It will dump you into a Python shell after having requested the page and parsing it. Once in the shell, you can do things with the response object as if you were in your spider. The shell also offers a shortcut function called fetch() that lets you pull up a different page.

  ex:

    fetch('https://freeweibo.com/en/')
    view(response) - see the page fecthed 
    Use xpath selectors 
    response.xpath(path) - tell scrappy what data to grab

    response.xpath("//div[@id='right']/ol/li/a/text()").extract() //xpath for the ol of the hotsearch

    response.xpath("//div[@id='right']/ol/li/a").extract() // get the links

    response.xpath("//div[@class='message censored-1 deleted-0']").extract() // for one post

Create Project:

  scrapy startproject freeweibo

    This will create a freeweibo directory with the following contents:

freeweibo/
    scrapy.cfg            # deploy configuration file

    freeweibo/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
            

Define the spider inside the spider folder. 

How to run spider:
  To put our spider to work, go to the project’s top level directory and run:

    scrapy crawl freeweibo

items.py

  The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. Spiders may return the     extracted data as items, Python objects that define key-value pairs.

pipelines.py

  After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it through several components that are executed sequentially. Connection is established with Database and items are sent to be stored on the database. 

References:

  https://docs.scrapy.org/en/latest/intro/tutorial.html //Scrapy Documentation Page

  https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3

  https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python

  https://coderslegacy.com/python/follow-links-in-scrapy/

  https://www.w3schools.com/xml/xpath_examples.asp

  https://www.youtube.com/watch?v=kkWhQKtxT2I&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=13
