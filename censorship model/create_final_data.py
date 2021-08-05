#encoding=utf-8
import csv
import jieba
import pandas as pd
import jieba.posseg as pseg


df1= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.labeled.csv', sep='\t')
#df1= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.labeled.csv', sep='\t', error_bad_lines=False)
#df2= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.segmented.csv', sep='\t')
df2= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.clean.processed.csv', sep='\t')

#print(df1)
#print(df2)
#print(df1['HotTerm'])
#print(df2['cleaned_content'])

df3 = pd.concat([df1['HotTerm'], df2['processed_content']], axis=1)
df3.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.final.data.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
