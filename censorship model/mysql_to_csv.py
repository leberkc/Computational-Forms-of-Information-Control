import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host="localhost", database = 'FreeWeibo',user="root", passwd="xxxxxxx",use_pure=True)
    query = "Select * from FreeWeiboPosts;"
    result_dataFrame = pd.read_sql(query,mydb)
    result_dataFrame.to_csv('freeweibo.raw.csv')
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))

