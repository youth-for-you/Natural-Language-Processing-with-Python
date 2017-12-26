#Find all the four-letter words in the Chat Corpus (text5).
# With the help of a frequency distribution (FreqDist),
# show these words in decreasing order of frequency.
from nltk.book import *
if __name__ == '__main__':
    fdist = FreqDist([w for w in text5 if len(w) == 4])
    #items()方法将字典的元素 转化为了元组，
    # 而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
    fdist = sorted(fdist.items(), key=lambda item:item[1], reverse=True)
    #排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
    print(fdist)
    print([w[0] for w in fdist ])


