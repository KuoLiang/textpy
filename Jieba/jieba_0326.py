# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import jieba
import jieba.analyse
from jieba import enable_parallel

text_poem = "白日依山盡,紅燒獅子頭,芋頭西米露,保力達蠻牛"
text_news = "二月下旬俄羅斯入侵烏克蘭，雙方爆發軍事衝突，歐美各國紛紛提出經貿制裁、金融封鎖與活動封殺等不同抵制手段，希望逼迫莫斯科停止軍事行動。在此同時西方各國領袖不斷透過協商，希望能夠透過採取具體共同行動，以便展現國家實力以及國際政治影響力；但卻在基本價值理念、歐美盟友體系以及取捨和戰思維上顯現出分歧與矛盾，此將對未來世局發展具有關鍵性作用。"
#jieba.set_dictionary('dict.txt')
#jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('user_dict.txt')

"""
ArithmeticErrorwb_poem1=jieba.cut(text_poem,cut_all=True)
wb_poem2=jieba.cut(text_poem,cut_all=False)
print("Full Mode Poem:","|".join(wb_poem1))
print("Default Mode Poem:","|".join(wb_poem2))

#%%
wb_news1=jieba.cut(text_news,cut_all=True)
wb_news2=jieba.cut(text_news,cut_all=False)
print("Full Mode News:","|".join(wb_news1))
print("Default Mode News:","|".join(wb_news2))

##########
#%%
tags_poem = jieba.analyse.extract_tags(text_poem, topK=5)
tags_news = jieba.analyse.extract_tags(text_news, topK=7)  
  
print(tags_poem)
print(tags_news)
"""
##########
#%%

content = open('input.txt', 'rb').read()
print("Input：", content)
wb_news3 = jieba.cut(content, cut_all=False)
print("Default Mode News:","|".join(wb_news3))
tags_news = jieba.analyse.extract_tags(content, topK=7) 
print(tags_news)







