#!/bin/bash

cd /myfolder/freeweibo
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl freeweibo
wait
scrapy crawl weiboTopicSearch
wait
scrapy crawl freeweibouser
