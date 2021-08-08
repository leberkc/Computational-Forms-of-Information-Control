#encoding=utf-8
import csv
import jieba
import pandas as pd
import jieba.posseg as pseg


df= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.final.data.csv', sep='\t')

#remove [" and '] from each row
df['processed_content'] = df['processed_content'].map(lambda x: x.lstrip('[').rstrip(']'))
df['processed_content'] = df['processed_content'].map(lambda x: x.lstrip('[').rstrip(']'))
df['processed_content'] = df['processed_content'].str.replace(r'[\'\"]*', '')


#df3 = pd.concat([df1['HotTerm'], df2['cleaned_content']], axis=1)
#print(df3)
#print(df3.replace({r'\\r': ''}, regex=True))
#df3 = df3.replace({r'\\r': ''}, regex=True)

df.to_csv(r'/home/leberkc/fastText/sandbox/junk.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
#df3.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.processed.txt', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
#print(df3)

