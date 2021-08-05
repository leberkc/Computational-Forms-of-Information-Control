#encoding=utf-8
import csv
import pandas as pd
freeweibo_labeled = pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.raw.csv')
freeweibo_labeled = freeweibo_labeled.dropna()
print(freeweibo_labeled)


from io import StringIO
col = ['row_id','Post_Id' ,'User_name','FreeWeibo_Post_Id','repostscount','censored','deleted','adult_keyword','censored_keyword','time_created','OriginalPostLink','HotTerm','content','time_scrapped']
freeweibo_labeled = freeweibo_labeled[col]
freeweibo_labeled = freeweibo_labeled[pd.notnull(freeweibo_labeled['content'])]
freeweibo_labeled.columns = ['row_id','Post_Id' ,'User_name','FreeWeibo_Post_Id','repostscount','censored','deleted','adult_keyword','censored_keyword','time_created','OriginalPostLink','HotTerm','content','time_scrapped']

freeweibo_labeled['HotTerm']=['__label__'+str(s).replace(' or ', '$').replace(', or ','$').replace(',','$').replace(' ','_').replace(',','__label__').replace('$$','$').replace('$',' __label__').replace('___','__') for s in freeweibo_labe
led['HotTerm']]
freeweibo_labeled['HotTerm']

freeweibo_labeled['content']= freeweibo_labeled['content'].replace('\n',' ', regex=True).replace('\t',' ', regex=True)

freeweibo_labeled.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.labeled.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
#freeweibo_labeled.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.labeled.txt', index=False, sep=' ', header=False, quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
