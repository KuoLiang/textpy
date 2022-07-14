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
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  
def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist('stopwords.txt')  # 這裏加載停用詞的路徑  
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:  
            if word != '\t':  
                outstr += word  
                outstr += " "   #再次組合成【帶空格】的串
    return outstr  

###########
#files
###########

inputs = open('input.txt', 'r', encoding='utf-8')  
outputs = open('output.txt', 'w')  
for line in inputs:  
    line_seg = seg_sentence(line)  # 這裏的返回值是字符串  
    outputs.write(line_seg + '\n')  
outputs.close()  
inputs.close()  

content_orig = open('input.txt', 'rb').read()        #without stopwords
content_stop = open('output.txt', 'rb').read()

###########
#show in console
###########


#print("Input：", content)
wb_news3 = jieba.cut(content_orig, cut_all=False)
wb_news4 = jieba.cut(content_stop, cut_all=False)

# 第一個參數：待提取關鍵詞的文本
# 第二個參數：返回關鍵詞的數量，重要性從高到低排序
# 第三個參數：是否同時返回每個關鍵詞的權重
# 第四個參數：詞性過濾，爲空表示不過濾，若提供則僅返回符合詞性要求的關鍵詞

#print("Default Mode News:","|".join(wb_news3))
tags_news3 = jieba.analyse.extract_tags(content_orig, topK=10, withWeight=True, allowPOS=()) 
#print(tags_news3)
# 同樣是四個參數，但allowPOS默認爲('ns', 'n', 'vn', 'v')
# 即僅提取地名、名詞、動名詞、動詞
tags_news4 = jieba.analyse.extract_tags(content_stop, topK=10, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v')) 
#tags_news4 = jieba.analyse.extract_tags(content_stop, topK=10, withWeight=True, allowPOS=()) 

#print(tags_news4)

for item in tags_news4:
    # 分別爲關鍵詞和相應的權重
    print(item[0], item[1])







