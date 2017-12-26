#python 3，nltk 3
import nltk
from nltk.book import *
if __name__ == '__main__':
    print()
    print(text1)
    #A concordance permits us to see words in context.
    # concordance搜索显示关键词及部分上下文
    text1 .concordance('monstrous')
    #similar寻找text1中与‘monstrous’上下文相似的单词
    text1.similar('monstrous')
    #common_contexts()研究共用多个单词的上下文
    text2.common_contexts(['monstrous', 'very'])
    #画出词汇分布一篇文章单词的出现位置。
    text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
    #产生随机文本，但是在nltk3不可用，在后续版本可用
    #text3.generate()
