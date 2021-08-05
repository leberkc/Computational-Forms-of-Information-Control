#encoding=utf-8
import csv
import jieba
import pandas as pd
import re
import jieba.posseg as pseg


df= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.raw.csv')
#df= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.labeled.csv',sep='\t', lineterminator='\r')

segmented_content = []
for i in df.index:
    post = df['content'][i]
    words = jieba.lcut(post,cut_all=True)
    segmented_content.append(words)

df['segmented_content']=segmented_content
#print(segmented_content)
##df['segmented_content']=segmented_content
###print(df['segmented_content'])
#print(df)

df.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.segmented.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
#df.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.segmented.txt', index=False, sep=' ', header=False, quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
