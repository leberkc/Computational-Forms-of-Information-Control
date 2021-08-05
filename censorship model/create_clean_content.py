import csv
import pandas as pd
import re
import jieba

def getChinese(df):
#    context = context.decode("utf-8") # convert context from str to unicode
    chinese = []
    for i in df.index:
        post = df['segmented_content'][i]
        words = re.sub(u'[^\u4E00-\u9FA5]', "", post) # non-Chinese unicode range
#        words = jieba.lcut(post,cut_all=True)
        chinese.append([words])
#    filtrate = re.compile(u'[^\u4E00-\u9FA5]') # non-Chinese unicode range
#    context = filtrate.sub(r'', str(context)) # remove all non-Chinese characters
#    context = context.encode("utf-8") # convert unicode back to str
    return chinese


def main():
    df= pd.read_csv('/home/leberkc/fastText/sandbox/freeweibo.segmented.csv', sep='\t')
#    print(df)
    context = getChinese(df)
#    print(len(context))
    df['cleaned_content'] = context
    df.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.clean.content.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
#    print(df)
'''
#Remove links
    context = re.sub("http://[a-zA-z./\d]*","",str(context))

    #Remove emoji
    context = re.sub("\[.{0,12}\]","",str(context))

    #Extract and remove tags
    tags = re.findall("#(.{0,30})#",str(context))
    context = re.sub("#.{0,30}#","",str(context))

    #Remove English characters
    english = re.findall("[a-z]+",str(context))
    context = re.sub("[a-z]+","",str(context))

    #Remove spaces
    context = re.sub("\s","",str(context))

    print(context)
    df['cleaned_content']  = context
    print(df)

    df.to_csv(r'/home/leberkc/fastText/sandbox/freeweibo.clean.content.csv', index=False, sep='\t', quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
'''
if __name__ == "__main__":
    main()
