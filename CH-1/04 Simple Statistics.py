from nltk.book import *
if __name__ == '__main__':
    #Frequency Distributions
    #liyong freqDist求出文中单词出现频率最高的50个单词
    fdist1 = FreqDist(text1)
    print(fdist1)
    print(fdist1.most_common(50))
    #单个单词出现频率
    print(fdist1['whale'])
    #我们或许可以通过高频词汇来了解文章的主题或风格，或许没有帮助。
    #3.2 我们可以Fine-grained Selection of Words来试试
    #输出颗粒大于15的单词
    V = set(text1)
    long_words = [w for w in V if len(w) >15]
    print(sorted(long_words))

    #3.3   Collocations and Bigrams
    #获取双连词bigrams（）
    bigrams_list =[]
    bigrams_list = list(bigrams(['more', 'is', 'said', 'than', 'done']))
    print(bigrams_list)
    #使用collocations()找到更加频繁的双连词（搭配）
    print(text4.collocations())