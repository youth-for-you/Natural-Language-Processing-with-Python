#Produce a dispersion plot of the four main protagonists
# in Sense and Sensibility:#Elinor, Marianne, Edward, and Willoughby.
#What can you observe about the different roles played by the males
# and females in this novel? Can you identify the couples?

from nltk.book import *
if __name__ == '__main__':
    #Sense and Sensibility是text2
    text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])
    '''
    由这些词的分布图我们可以看到Elinor, Marianne两个词贯穿全文应该是两个女主角，
    而Edward, and Willoughby两个人穿插在文中，推测应该是Elinor和Edward一对，另外两人一对。
    '''