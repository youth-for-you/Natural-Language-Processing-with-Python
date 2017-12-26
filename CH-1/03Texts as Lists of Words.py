#将文本当做词链表
from nltk.book import *

def lexical_diversity(text):
    # 返回词汇丰富比
    return len(set(text)) / len(text)
if __name__ == '__main__':
    #2.1 Lists
    sent1 = ['call', 'me', 'Ishael', '.']
    sent2 = ['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']
    print(sent1)
    #输出链表长度
    print(len(sent1))
    #词汇丰富度
    print(lexical_diversity(sent1))
    #链表的+操作
    print(sent1+sent2)
    #链表添加一个元素
    sent1.append('some')
    print(sent1)

    #2.2 Indexing Lists
    print(text4[173])
    #输出awaken在文中的位置
    print(text4.index('awaken'))
    #切片，抽取文章
    print(text5[16715:16735])
    sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
    #切片替换
    sent[1:9] = ['Second', 'Third']
    print(sent)

    #2.3 Variables
    #2.4 Strings
    name = 'Monty'
    #切片功能
    print(name[:4])
    #字符串乘法和加法
    print(name * 2 + '!')
    #split()按空格切分
    print('I Love Python !'.split())
