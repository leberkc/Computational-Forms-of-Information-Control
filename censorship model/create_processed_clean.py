#encoding=utf-8
import csv
import jieba
import pandas as pd
import re
import jieba.posseg as pseg


df= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.processed.csv', sep='\t')
#df= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.labeled.csv',sep='\t', lineterminator='\r')
#print(df['cleaned_content'])

processed_content = []
for i in df.index:
    post = df['cleaned_content'][i]
    words = jieba.lcut(post,cut_all=True)
    processed_content.append(words)

df['processed_content']=processed_content
#print(df)

df.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.clean.processed.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
