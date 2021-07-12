# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import mysql.connector


class FreeweiboPipeline(object):
    def __init__(self):
        self.create_connection()
        
        self.curr.execute("SELECT FreeWeibo_Post_Id FROM FreeWeiboPosts")
        unique_postId = self.curr.fetchall()
        self.ids_seen = unique_postId

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Itagui22388!',
            database = 'FreeWeibo'
            )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        if adapter['postid'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.store_post_db(item)
            return item

    def store_post_db(self, item):
        post_values =[
            item['username'], 
            item['postid'], 
            item['repostscount'], 
            item['censored'], 
            item['deleted'], 
            item['contains_adult_keyword'], 
            item['contains_censored_keyword'], 
            item['time_created'], 
            item['freeweiboOGpostlink'], 
            item['hotterm'], 
            item['content'], 
            item['timestampPostscrapped']
        ]

        self.curr.execute(
            "INSERT INTO FreeWeiboPosts VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",post_values
            )
        self.conn.commit()

