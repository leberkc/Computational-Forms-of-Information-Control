# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class FreeweiboPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'admin',
            passwd = 'freeweibo2021',
            database = 'FreeWeiboPosts'
            )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        values =[
            item['username'], 
            item['postid'], 
            item['repostscount'], 
            item['censored'], 
            item['deleted'], 
            item['contains_adult_keyword'], 
            item['contains_censored_keyword'], 
            item['time_created'], 
            item['freeweiboOGpostlink'], 
            item['content'], 
            item['hashtags'][:], 
            item['hashtagsurls'][:], 
            item['timestampscrapped']
        ]
        self.curr.execute(
            "INSERT INTO Posts VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",values
            )
        self.conn.commit()
