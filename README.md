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
* Create the second spider `weibo_user_data_scraper.py` in the `spiders` folder.
	* This spider calls Weibo API using the users id from freeweibo to collect users data. 
* Create the third spider `weibo_topicSearch.py` in the `spiders` folder.
	* This Spider searches Weibo's timeline using the hot term from FreeWeibo's Real-time hot search and collects the posts and users data. 

### Modify Items
* Spiders will return extraced data as items. 
* Modify `items.py`.

### Modify Pipelines
* After the items have been scraped by the spiders, it will be sent to the Item Pipeline which processes using several components that are executed sequentially. 
* Modify `pipelines.py`.

### Modify Settings
* The Scrapy settings allows you to customize the behavior of all Scrapy components, extensions, pipelnes and spiders. 
* Modify `settings.py`.

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
