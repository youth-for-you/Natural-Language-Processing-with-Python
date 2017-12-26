#Define a variable my_sent to be a list of words,using the syntax my_sent = ["My", "sent"]
# (but with your own words, or a favorite saying).
#Use ' '.join(my_sent) to convert this into a string.
#Use split() to split the string back into the list form you had to start with.

if __name__ == '__main__':
    my_sent = ['I', 'Love', 'Python', '!']
    # join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    str_my_sent = ' '.join(my_sent)
    print(str_my_sent)
    #输出I Love Python !
    list_my_sent = str_my_sent.split()
    print(list_my_sent)
    #输出['I', 'Love', 'Python', '!']
