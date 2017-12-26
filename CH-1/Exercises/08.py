#Consider the following Python expression: len(set(text4)).
#State the purpose of this expression. Describe the two steps
#  involved in performing this computation.
from nltk.book import *
if __name__ == '__main__':
    print(text4)
    #set（text4）获取text4不重复单词集合
    print(set(text4))
    #len(set(text4))获取text4 不重复词汇的数量（长度）
    print(len(set(text4)))