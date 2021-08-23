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
            database = 'FreeWeibo'
            )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        
        if spider.name == 'freeweibo':

            values = [item['hotterm']]

            self.curr.execute("""
            SELECT HotTerm
            FROM HOTTERMS  
            WHERE HotTerm = (%s)
            """, values)

            result = self.curr.fetchall()

            if self.curr.rowcount >= 1:
                self.store_update_hotterms_db(item)
                self.store_post_db(item)
                return item
            else:
                self.store_hotterms_db(item)
                self.store_post_db(item)
                return item

        if spider.name == 'freeweibouser':

            if item['active_status'] is False:
                self.store_freeweibo_inactive_user_db(item)
                return item
            else:
                self.store_freeweibo_user_db(item)
                return item

        if spider.name == 'weiboTopicSearch':
            self.store_weibo_post_db(item)
            self.store_weibo_user_db(item)
            return item

        if spider.name == 'oneprocessfreeweibo':

            values = [item['hotterm']]

            self.curr.execute("""
            SELECT HotTerm
            FROM HOTTERMS  
            WHERE HotTerm = (%s)
            """, values)

            result = self.curr.fetchall()

            if self.curr.rowcount >= 1:
                self.store_update_hotterms_db(item)
                self.store_post_db(item)
                if item['active_status'] is False:
                    self.store_freeweibo_inactive_user_db(item)
                else:
                    self.store_freeweibo_user_db(item)
                return item
            else:
                self.store_hotterms_db(item)
                self.store_post_db(item)
                if item['active_status'] is False:
                    self.store_freeweibo_inactive_user_db(item)
                else:
                    self.store_freeweibo_user_db(item)
                return item

    def store_post_db(self, item):
        post_values =[
            item['username'], 
            item['weibo_user_id'],
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
            """INSERT INTO FreeWeiboPosts 
            VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",post_values
            )
        self.conn.commit()

    def store_hotterms_db(self, item):
        post_values =[
            item['hotterm'], 
            item['timestampPostscrapped'],
            item['timestampPostscrapped']
        ]

        self.curr.execute(
            "INSERT INTO HOTTERMS VALUES (NULL,%s,%s,%s)",post_values
            )
        self.conn.commit()

    def store_update_hotterms_db(self, item):

        values =[
            item['timestampPostscrapped'],
            item['hotterm']
        ]

        self.curr.execute(
            """UPDATE HOTTERMS 
            SET last_time_scrapped = (%s)
            WHERE HotTerm = (%s)
            """, values)

        self.conn.commit()

    def store_freeweibo_user_db(self, item):
        user_values =[
            item['weibo_user_id'],
            item['screename'],
            item['profile_url'], 
            item['statuses_count'],  
            item['verified'],
            item['verified_type'],
            item['verified_reason'],
            item['close_blue_v'], 
            item['u_description'], 
            item['gender'], 
            item['mbtype'],
            item['urank'], 
            item['mbrank'], 
            item['follow_me'],
            item['following'],
            item['followers_count'],
            item['follow_count'],
            item['origin'],
            item['active_status'],
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO FreeWeibo_User_data 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ,user_values)
        self.conn.commit()

    def store_freeweibo_inactive_user_db(self, item):
        user_values =[
            item['weibo_user_id'],
            item['active_status'],
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO FreeWeibo_User_data (weibo_user_id,active_status,time_scrapped) 
            VALUES (%s,%s,%s)"""
            ,user_values)
        self.conn.commit()

    def store_weibo_post_db(self, item):
        post_values =[
            item['hotterm'],
            item['post_id'],
            item['mid'],
            item['created_at'], 
            item['content'],
            item['textLength'],  
            item['source'],
            item['favorited'],
            item['weibo_user_id'],
            item['reposts_count'],
            item['comments_count'], 
            item['attitudes_count'], 
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO Weibo_HotTerm_Topic_Post 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ,post_values)
        self.conn.commit()

    def store_weibo_user_db(self, item):
        user_values =[
            item['weibo_user_id'],
            item['screename'],
            item['profile_url'], 
            item['statuses_count'],  
            item['verified'],
            item['verified_type'],
            item['verified_reason'],
            item['close_blue_v'], 
            item['u_description'], 
            item['gender'], 
            item['mbtype'],
            item['urank'], 
            item['mbrank'], 
            item['follow_me'],
            item['following'],
            item['followers_count'],
            item['follow_count'],
            item['origin'],
            item['time_scrapped']
        ]

        self.curr.execute(
            """INSERT INTO Weibo_User_data 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ,user_values)
        self.conn.commit()
