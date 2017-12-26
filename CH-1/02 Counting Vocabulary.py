from nltk.book import *

if __name__ == '__main__':
    #输出文章长度
    print(len(text3))
    #set单词不重复集合
    print(set(text3))
    #排序输出sorted
    print(sorted(set(text3)))
    #set集合长度
    print(len(set(text3)))
    #文章词汇丰富度测量
    print(len(set(text3)) / len(text3))
    #输出某一单词的出现次数
    print(text3.count('smote'))
    #单词出现占文百分比
    print(100 * text4.count('a') / len(text4))
    #Q：How many times does the word lol appear in text5?
    # How much is this as a percentage of the total number of words in this text?
    print(text5.count('lol'))
    print(100 * text5.count('lol') / len(text5))


    # 建立函数解决重复计算输入
    def lexical_diversity(text):
        # 返回词汇丰富比
        return len(set(text)) / len(text)


    def percentage(count, total):
        # 返回词百分比
        return 100 * count / total
    #eg:
    print(lexical_diversity(text3))
    print(lexical_diversity(text5))
    print(percentage(text4.count('a'), len(text4)))
