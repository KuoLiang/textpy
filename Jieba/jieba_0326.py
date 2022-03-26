# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import jieba
import jieba.analyse

text_poem = "白日依山盡紅燒獅子頭芋頭西米露保力達蠻牛"
text_news = "二月下旬俄羅斯入侵烏克蘭，雙方爆發軍事衝突，歐美各國紛紛提出經貿制裁、金融封鎖與活動封殺等不同抵制手段，希望逼迫莫斯科停止軍事行動。在此同時西方各國領袖不斷透過協商，希望能夠透過採取具體共同行動，以便展現國家實力以及國際政治影響力；但卻在基本價值理念、歐美盟友體系以及取捨和戰思維上顯現出分歧與矛盾，此將對未來世局發展具有關鍵性作用。"
#jieba.set_dictionary('dict.txt')
jieba.load_userdict('user_dict.txt')

wb_poem=jieba.cut(text_poem,cut_all=True)
wb_news=jieba.cut(text_news,cut_all=True)
print("Full Mode:","|".join(wb_poem))
print("Full Mode:","|".join(wb_news))
#####
wb_poem=jieba.cut(text_poem,cut_all=False)
wb_news=jieba.cut(text_news,cut_all=False)
print("Default Mode:","|".join(wb_poem))
print("Default Mode:","|".join(wb_news))

##########



