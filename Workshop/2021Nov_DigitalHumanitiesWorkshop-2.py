#!/usr/bin/env python
# coding: utf-8

# # 2021.11.25 數位人文社會科學創新教學計畫工作坊
# # Python與其在文件蒐尋及文本分析的應用：一個語言學家的觀點
# 
# - 內容大綱：
# 1. 介紹Python本體的知識：
#    1. Python物件，包括：字串(string)、數字(number)、表列(list)、有序組(元組，tuple)、字典(dictionary)、集合
#    2. 模組載任(import)
#    3. 迴圈：for、while
#    4. if 條件判斷
#    5. 函式 (function)
# 2. 利用正表達式模組(regular expression, re)來進行文件蒐尋
# 3. 文件情感分析
# 
#     
# ## 變數、數字(number)、簡單數學運算
# 
# - 變數(variable)的作用，有點像是自然語言中的代名詞，作用就是指涉某個事物。
# - 在Python中，變數命名有以下規則：
#     1. 要有意義：方便多人共同開發及/或日後檢視程式碼 (不是Python語言的語法規定)
#     1. 以下為Python的語法規定：
#         1. 必須以英文字母開始
#         1. 變數名稱，只限英數底線及中文，不過，很少用中文來當變數，因為需要英文、中文切換
#         1. 大小寫視為不同
#         1. 避免保留字元，如：print, open, if, while, input, else, and, or等。
# - 在Python中，不需要事先宣告要使用哪些變數及變數的類型(type)，只要在要使用某變數時，將值(不限於數值)指派給該變數即可。
# - 為什麼要使用變數？
#     1. 當值很長，而且需要重複使用時
#     1. 某個函式(function)的計算結果，要傳給其他函式使用時
# - 我們來看幾個例子：

# In[2]:


print('This is a book. That is a pen'.split())
print('this is a book. That is a pen.'.index('i'))


# In[3]:


string1 = "This is a book. Tha tis a pen."
print(string1.split())
print(string1.index("i"))


# - 沒有規定一個程式中，可以用幾個變數。
# - 只要有必要用變數，就可以使用變數。
# - 你可以把舊的變數指派新值，從該項指派後，那個變數就以新的值的面貌出現，舊的值就與其無關了。
# - 你也可以用 del Var來刪除某變數。但Python並不硬性規定要這樣做。這也是Python為什麼允許：A = A + B 這種看起來有點怪的計算式了。
# - Python中的變數，有幾點要記得：
#     1. 變數只有在指派值之後才存在。故，不需事先宣告變數。
#     1. 變數本身沒有類型(type)，變數的值才有類型。故，不需事先宣告變數的類型。
#     1. 變數的名稱，大寫小有別。

# ### 基本數學運算

# In[13]:


print("加法：", 3+4)
print("減法：", 45-33)
print("乘法：", 3*8)
print("次方：", 2**3)                     # n ** m 是n的m次方的意思
print("次方：", 9**0.5)                   # 也可以利用 ** 來做根號運算
print("除法：", 8/2)
print("除法：", 10/3)
print("四捨五入：", round(10/3))           # 四拾五入
print("取商數:", 10//3)                    # 只計算商數，不做四拾五入
print("取餘數:", 0%3)                      # 取餘數
print("小數點乘法：", 102.33*44.65)        # 小數點也可以
print("絕對值：", abs(345))                # 絕對值
print("絕對值：", abs(-345))
print("次方：", pow(2,10))                          # pow(n, m) n的m次方


# ### Python數學運算的優先順序 (precedence)
# 
# - 在學數學時，大家都學過：先乘除，後加減。這是同一個計算式中，既有乘除又有加減時的計算順序。
# - Python的數學運算也遵守相同的順序。
# - Python的數學運算順序如下：
#     1. 次方
#     2. 乘、除、求餘數、求整數商。如果是這幾個在同一計算式中，則依出現順序計算。
#     3. 加減。如果出現於同一式中，則依出現順序計算。
# - 可以使用圓括號(小括號)來強制優先運算。

# In[5]:


print(2+3*3)
print(100/2*30//4)
print((2+3)*3)
print(100/(2*30)//4)
print(2**4+5)
print(2**(4+5))


# ## math 模組
# 
# - Python一個很強大的優勢，就是有很多很多的模組可以很快地、很簡單地處理很多的工作。
# - 有些模組是內建的，也就是你下載Python時就有了，有些則要在需要時另外下載安裝。
# - math就是一個內建的數學模組，可以簡單地做很多數學運算。
# - 你可以在：https://docs.python.org/3.7/library/math.html 找到math這個模組的所有可使用的函式(function)。
# - 看以下幾個簡單的例子：

# In[6]:


import math    # 模組需要載入才能使用

print(math.sqrt(100))        # 平方根
print(math.pow(5, 4))        # math.pow(n, m) 計算 n 的 m 次方
print(math.factorial(10))    # math.factorial(n) 計算 n 的階層 (n!)


# In[7]:


print(math.floor(3.5))
print(math.floor(-3.5))      # math.floor(n)回傳比n小或等於n的整數
print(math.trunc(3.2))
print(math.trunc(3.7))       # 無條件捨去


# In[8]:


print(round(3.2))
print(round(3.7))            # 四拾五入，round()不在math模組中！
print(round(4.553421, 3))    # 取到小數第三位


# In[9]:


print(math.pi)               # 還有一些內建的、數學上常用到的常數
print(math.e)


# ### 練習一下
# 
# 1. 假設你收集到一個小baby說的六個句子：up、come up、play ball、come play ball、daddy come play ball、daddy play ball、daddy play too。你想要計算一下這個baby的 MLU (Mean Length of Utterance)。你應該怎麼做？(使用下面Excercise 1的部份程式碼)
#     1. 如果你的MLU要取到小數點下兩位，四捨五入，該怎麼做？
#     2. 如果你的MLU要小數點下無條件捨去，該怎麼做？
# 2. 假設你有一篇英文短文，你想要計算the佔整篇短文字數的百分比，應該怎麼做？(使用Exercise 2的部份程式碼) 四取五入，取到小數點第四位。

# In[ ]:


# Ex. 1

import math

utter1 = ['up']
utter2 = ['come', 'up']
utter3 = ['play', 'ball']
utter4 = ['come', 'play', 'ball']
utter5 = ['daddy', 'come', 'play', 'ball']
utter6 = ['daddy', 'play', 'ball']
utter7 = ['daddy', 'play', 'too']

lenUtter1 = len(utter1)     # 用len()來取得一個成員有順序的物件的成員個數
print(lenUtter1)


# In[15]:


# Exercise 2

#from nltk.tokenize import word_tokenize

article = "The government’s travel notice for South Korea has been raised to a level 3 “warning” — avoid all nonessential travel — due to a jump in the number of COVID-19 cases there, the Central Epidemic Command Center (CECC) said yesterday, adding that two more cases have been confirmed in Taiwan. The community spread of the virus in South Korea has been shown by the rapid increase in confirmed cases in the past few days, which totaled 763 yesterday, Minister of Health and Welfare Chen Shih-chung (陳時中) said.“As the risk of infection is elevated in the country, the center decided to raise the travel notice to level 3,” said Chen, who serves as the center’s head. “We recommend people avoid all nonessential travel.”"

#words = word_tokenize(article)

words = ['The', 'government', '’', 's', 'travel', 'notice', 'for', 'South', 'Korea', 'has', 'been', 'raised', 'to', 'a', 'level', '3', '“', 'warning', '”', '—', 'avoid', 'all', 'nonessential', 'travel', '—', 'due', 'to', 'a', 'jump', 'in', 'the', 'number', 'of', 'COVID-19', 'cases', 'there', ',', 'the', 'Central', 'Epidemic', 'Command', 'Center', '(', 'CECC', ')', 'said', 'yesterday', ',', 'adding', 'that', 'two', 'more', 'cases', 'have', 'been', 'confirmed', 'in', 'Taiwan', '.', 'The', 'community', 'spread', 'of', 'the', 'virus', 'in', 'South', 'Korea', 'has', 'been', 'shown', 'by', 'the', 'rapid', 'increase', 'in', 'confirmed', 'cases', 'in', 'the', 'past', 'few', 'days', ',', 'which', 'totaled', '763', 'yesterday', ',', 'Minister', 'of', 'Health', 'and', 'Welfare', 'Chen', 'Shih-chung', '(', '陳時中', ')', 'said.', '“', 'As', 'the', 'risk', 'of', 'infection', 'is', 'elevated', 'in', 'the', 'country', ',', 'the', 'center', 'decided', 'to', 'raise', 'the', 'travel', 'notice', 'to', 'level', '3', ',', '”', 'said', 'Chen', ',', 'who', 'serves', 'as', 'the', 'center', '’', 's', 'head', '.', '“', 'We', 'recommend', 'people', 'avoid', 'all', 'nonessential', 'travel', '.', '”']

articleLeng = len(article)

numThe = words.count('the')


# ## 字串 (string)
# 
# - 字串是由一連串的字元(characters)所構成的物件，字元本身沒有意義。
# - 字串中的字元可以是：羅馬字母、數字、鍵盤上的許多功能鍵，如空白鍵、enter鍵等，或是世界上任何語言的字母、文字(如：漢語中的方塊字)
# - 在 Python 中，字串的標示為：引號，可以單引號、雙引號、三個單/雙引號。

# In[17]:


s1 = 'this is a book'
s2 = "that's a pen, not a pencil"
s3 = ''' this is a book.         # 使用三個單/雙引號，可以換行
not a pen. That is a pen, 
not a pencil'''

print(len(s1))              # 可以用len()來求取字串長度(=有幾個字元)。
print(len(s2))              # 注意：這個長度包含了所有字元，包括：空白、標點、特別符號等。
print(len(s3))


# In[18]:


print('this '* 50)            # 用乘的符號來做(整個)字串重複
print('this ' + 'is a book')  # 用加的符號來做字串前後相連
print(4456+678)               # 注意數字加法與字串"加法"的不同！
print('4456'+'678')


# ### 字串位址(index)\[索引\]與切段(slicing)
# 
# - 字串是一種成員順序有關係的Python物件，也就是，成員順序不同，會產不同的字串。
# - 同樣是成員順序有關係的Python物件有：表列(list)、有序組(tuple)
# - 既然成員順序是有關係的，我們可以利用成員的位址(index)來直接取得該成員。
# - 也可以用切段(slicing)的方式，取得字串中某一小段的成員。
# - 如：

# In[19]:


s = 'John saw a girl with a telescope; Mary hit a boy with a stick.'
print(s[0])                # 用方括號來標示位址，位址以 0 開始！
print(len(s))
print(s[61])               # 最後一個字元的位址是長度-1
print(s[-1])               # 也可以用 -1 來代表最後一個字元
print(s[2:6])              # 從位圵2到位址5；string[n:m] 從位址 n 到位址 m-1
print(s[:10])              # 冒號前留白，表示從頭開始
print(s[50:])              # 冒號後留白，表到取到最後一個字元
print(s[0:20:4])           # 每隔3個字元取一個字元，取到位址19的字元
print(s[61:30:-2])         # 從最後一個字元開始，往前取，每隔一個字元取一個字元
print(s[30:60:-2])         # 使用負號來做反向選取，前面的位址亦需反向標明 (因為沒有結果，故印出的是空白行)


# ### 字串方法 (string method)
# 
# - Python提供了處理字串的一些方便、快速的功能，這些叫：字串方法 (string method)。
# - 你可以用 help('') 來列出所有的字串方法。註：''是空字串，一個沒有任何字元的字串；' '是一個長度為1的字串，其只包括一個字元：空白。
# - 使用字串方法的格式：要處理的字串.方法()
# - 查詢所有字串方法：help('')

# In[20]:


s5 = 'phonotactics'
print(s5.capitalize())          # 第一個字母大寫
print(s5.upper())               # 全部字母大寫
print('THIS IS A book'.lower()) # 把大寫字母變小寫


# In[21]:


print(s5.count('o'))            # 計算特定字串中的某個字元出現的次數
print(s5.count('o', 0, 4))      # 可以計算指定特定字串中的次字串中某字元出現的次數
print(s5.endswith('s'))         # 判斷某字串是否以特定某個/些字元結束
print(s5.endswith('cs'))
print(s5.endswith('c'))


# In[22]:


print(s5.isalnum())             # 判斷字串是否為字母或/及數字
print('052720411CCU'.isalnum())
print(' '.isalnum())            # 空白不是字母或數字
print('this is a book'.isalnum())
print('this\tis'.isalnum())
print('你好嗎'.isalnum())       # 中文字視為字母
print('你好嗎？'.isalnum())     # 全形標點不是字母


# In[23]:


print('this is a book.'.isascii())  # 判斷是否為 ASCII 字元 (編碼號碼在 128 之前)，空白換行什麼的都算
print('你好嗎'.isascii())       # 中文字不是 ASCII
print('8.45'.isdecimal())      # 小數點不是，整數才是 
print('897'.isdecimal())
print('4.56'.isdigit())        # 判斷字串是否都是數字，不能有數字以外的字元
print('456'.isdigit())


# In[24]:


print('THIS'.isupper())        # 判斷字串中的字元是否全為大寫
print('This'.isupper())
print('this'.islower())        # 判斷字串中的字元是否全為小寫
print('This'.islower())
print(' '.join(['this', 'is', 'a', 'book']))  # 把一個表列或有序組成員組合成一個完整字串


# In[25]:


print('This is a book'.lstrip('Th'))  # 剝掉最左邊的指定字元，如果最左邊沒有指定的字元，則回傳原字串
print('This is a book'.lstrip('a'))   # 另有一個 .strip()，功能相同，只是處理最右邊的字元
print('   this is a book'.lstrip())   # 如果沒有指定要剝除的字元，則會刪除空白、tab、換行等字元
print('   this is a book    '.rstrip())  # .rstrip()作用與上同，只是是剝右邊的


# In[26]:


print('this is a book'.split())          # 未標示分隔字元，則依空白分割字串。注意：有n個空白就可以分出n+1個字串
print('phonotactics'.split('o'))         # 把 o 之前、之後的拆出獨立成字串，但o本身不會出現，輸出是一個字串構成的表列
print('This is a book.\nThat is a pen.\nWeird Stuff.'.splitlines())    # 依換行符號做分割，回傳一個表列


# ### 練習
# 
# 1. 下面的EngNews是一段從USA Today上擷取的新聞，已經以字串類型指派給EngNews這個變數。請執行下面動作：<br>
#     (1) 將這則新聞拆成一個一個的詞，以表列形式儲存。<br>
#     (2) 將這則新聞拆成一行一行，以表列形式儲存。<br>
#     (3) 將上面拆出的第一行，變為標題格式。(註：表列與字串相同，可以位址來取得成員。第一行的位址是...？)<br>
#     (4) 把第二行的右邊about.刪除，左邊的During也刪除。<br> 
#     (5) 對第三行做以下工作：(a) 是不是以 I 開始？(b) 是不是由字母或數字組成？ (c) 是不是ASCII？ (d) 通通轉為大寫
# 1. 假設我們有以下三個字串：張三李四、張三101李四、張三John，怎麼可以判斷，那個字串只包含漢字？

# In[ ]:


EngNews = '''Trump asks for payroll tax relief despite GOP hesitance
During his Wednesday night speech, Trump asked that Congress consider payroll tax cuts – a request that lawmakers in both parties have voiced concern about. 

"I am calling on Congress to provide Americans with immediate payroll tax relief," Trump said. "Hopefully, they will consider this very strongly. We are at a critical time in the fight against the virus."

The idea has been met with skepticism in recent days from even Republicans, who call the idea both premature and something that would not help in this situation. 

"I would prefer they exercise other options before going down that path," Sen. John Thune, the No. 2 Republican in the Senate has said. Democrats have said the idea is something that would have no chance in passing the Democratic-held House. 

"It's a non-starter," Majority Leader Steny Hoyer, the No. 2 Democrat in the House said earlier Wednesday of the payroll tax cut idea. '''


# ## 表列 (list) \[串列\]
# 
# - 表列(list)是Python中使用頻率很高的一種結構，用來儲存資料供運算，或是儲存運算之後的資料。
# - 表列由方括號 \[\]標示，其中的成員由逗號(,)分隔。表列的成員是有順序性的，也就是相同成員、但成員排列順序不同，是不同表列。
# - 表列的成員沒有類型的限制，也沒有類型一致性的要求。也就是說，任何Python類型的物件都可以做為表列的成員。而表列的成員，也不需要在類型上一致，也就是說，表列的成員不需要是相同類型。
# - 注意：
#     1. 字串的基本單位是字元，而表列的基本單位是由逗點隔開的成員。這點在做for迴圈時，會有不同。
#     1. 表列是mutable，意思是：可以立刻改變其所構成的成份 (= in-place change)，而字串是immutable，也就是不能改變其構成成份。
# - 如： 

# In[ ]:


# 以下都是合法的表列

L1 = ['this', 'is', 'a', 'book']
L2 = [98, 66, 54, 60, 78, 80]
L3 = ['Allen Smith', 45, 34000, 'assistant manager']
L4 = [[1,2,3], 
      [4,5,6], 
      [7,8,9]]


# ### 表列的位址(index)與切片(slicing)
# 
# - 因表列是有順序性的，故可以使用位址和切片來取得其成員，與字串相同。
# - 見下例。

# In[2]:


L = list('thisisabook,notapen')

demos = [L, len(L), L[0], L[13], L[-1], L[-3], L[:8], L[14:], L[:10:2], L[-1:6:-3], 'o' in L, 'z' in L, 'z' not in L]

counter = 1

for demo in demos:
    print(f"{counter}: {demo}")
    counter+=1
'''
print(L)
print(len(L))                       # 表列 L 的長度(=有幾個成員)
print(L[0])                         # 第一個(位址 0)的成員
print(L[13])                        # 第十四個(位位 13)的成員
print(L[-1])                        # 最後一個成員
print(L[-3])                        # 倒數第三個成員
print(L[:8])                        # 從第一個到第八個(位址 7)成員，回傳一個表列
print(L[14:])                       # 從第十五個成員(位址 14)到最後一個，回傳一個表列
print(L[:10:2])                     # 從頭到第十個成員(位址 9)，每隔一個取一個，回傳表列
print(L[-1:6:-3])                   # 從最後一個往前到位址(6+1)的成員，每個 2 個取 1 個，傳回一個順序與 L 相反的表列。
print('o' in L)                     # 檢測某個成份是否為 L 的成員，回傳布林值
print('z' in L)
print('z' not in L)
'''
print()


# In[7]:


# 一些可以作用於成員為數值的表列的函式

L2 = list(range(1,100,3))

counter = 1
for f in [L2, max(L2), min(L2), sum(L2)]:
    print(f"{counter}: {f}")
    counter+=1
'''    
print(L2)
print(max(L2))                   # 取得表列中的最大值
print(min(L2))                   # 取得表列中的最小值
print(sum(L2))                   # 把表列的值都加起來
print(max(L))                    # 如果表列的成員是字串，則最大、最小值依表列成員的內碼決定
print(min(L))
'''
print()


# In[8]:


# 更改表列成員：表列允許直接改變其成員，而不會產成新的表列

L3 = ['John', 56, 'Mary', 49, 'Susan', 87, 'Mark', 88]
print(L3)
L3[0] = 'John Smith'                               # 直接改變第一個成員的值
print(L3)
L3[2:4] = ['Mary Carl', 80]                        # 可以改變一個切片的值
print(L3)
L3[8] = 'Jack'                                     # 但是，不能使用超過其長度的位址，也就是，如果要把新加到 L3 之後，要用其他方法
print(L3)


# In[9]:


L4 = ['趙敏', '小昭', '周芷若', '阿離', '郭襄', '完顏萍']
L5 = [1,2,3,4,5]
print(L4+L5)                        # 用 + 來把兩個表列前後相接
print(L4*2)                         # 用 * 來重覆表列的成員
print(L5*3)

# 注意：用 + 或 * 來運作於兩個表列，會產生一個新的表列
# 如果你需要用到這兩個運作的成果，必須將其指派給一個變數，
# 如：L45 = L4 + L5

del L4[3]                          # 刪除表列內的某個成員
print(L4)

del L5[:4]                         # 也可以刪除表列中的一個切片
print(L5)

# 注意：因為刪除成員後，對電腦而言，那個成員就好像從未存在過一樣
# 所以，如果要對表列做任何運作(包括但不限於刪除)，不妨把原來表列
# 複制一份，所有動作都做在複制版上，保留原始表列。

L4 = ['趙敏', '小昭', '周芷若', '阿離', '郭襄', '完顏萍']
newL4 = L4[:]
del newL4[1:3]
print('The original L4 is:', L4)
print('the processed L4 (newL4) is:', newL4)


# ### 表列方法 (method)
# 
# - 每種Python物件類型都有其自己的方法(method)，可以對該類型的物件做處理。
# - 我們見過字串方法了。現在來看看表列方法：

# In[10]:


L4 = ['趙敏', '小昭', '周芷若', '阿離', '郭襄', '完顏萍']
print(L4)

L4.append('程靈素')                        # 把新成員附加到原表列的末端
print(L4)
print(L4.append('胡若蘭'))                 # .append()直接改變了表列的內容，並未回傳新表列，故用print()無法印出任何東西
L4.extend(['胡若蘭', '駱冰', '阿碧'])      # 表一個表列的成員附加於另一表列之末 
print(L4)
L4.clear()                                # 刪除表列中所有成員
print(L4)
L4 = ['趙敏', '小昭', '周芷若', '阿離', '郭襄', '完顏萍']
L5 = L4.copy()                            # 如果表列的內容較複雜(如，包含多層的表列)，則不適用
print(L5)


# In[11]:


print(L4.index('阿離'))                   # 取得第一個指定成員的位址 (只有第一個哦！)
L4.insert(3, '任盈盈')                    # 在指定位址插入新成員，原成員往後移
print(L4)
print(L5.pop())                          # .pop()移除某一特定位址的成員，沒標明位址，則移除最後一個                
print(L5)                                # .pop()會回傳被刪除的成員
print(L5.pop(3))
print(L5)

L5.remove('周芷若')                      # .remove()指定要移除的成員的第一個。注意：不回傳任何值！
print(L5)

L5.reverse()                            # .reverse()直接把表列成員顛倒
print(L5)


# In[12]:


L6 = [34, 56, 12, 11, 3, 5, 99, 65]
L6.sort()
print(L6)                               # .sort()將表列中的值由小到大排列
L6 = [34, 56, 12, 11, 3, 5, 99, 65]
L6.sort(reverse=True)                   # 標明 reverse = True，則由大排到小
print(L6)

print(L)
L.sort()                                # 如果表列的內容是字串，則依字串的內碼大小排列
print(L)


# In[13]:


LL = list('thisisabooknotapenthatisapennotabook')
print(LL.count('i'))                    # .count()可以計算某成員出現的次數

L7 = ['abc', 'ABC', 'ABc', 'AbC', 'aBC', 'Abc']
print(L7)
L7.sort()
print(L7)
L7 = ['abc', 'ABC', 'ABc', 'AbC', 'aBC', 'Abc']
L7.sort(reverse=True)
print(L7)

L6 = [34, 56, 12, 11, 3, 5, 99, 65]
sorted(L6)                             # 也可以直接用內建的 sorted() 來做排序


# In[14]:


# 可以用enumerate()把位址與該位址的物件包裹成(位址，物件)的有序組

drinks = ['coffee', 'tea', 'wine', 'coke']
enumerate_drinks = enumerate(drinks)
print('Type of enumerate object: ', type(enumerate_drinks))
print('轉成表列：', list(enumerate_drinks))

e_drinks02 = enumerate(drinks, start = 10)  # 指定起始位址
print('轉成表列：', list(e_drinks02))


# In[15]:


# 因為表列可以當場改變其成員而不會產生新表列，
# 故表列常使用來儲存程式一步一步的產生的結果

# 如：我有一個表列，成員有的是全大寫，有的是全小寫，
# 我想把全大寫及全小寫的成員分開，要怎麼做？

L8 = ['AAA', 'cde', 'ZZZ', 'fds', 'LKD', 'wdk', 'IHJ', 'kid']

capitals = []            # 先指定兩個空表列給兩個變數，用來儲存待會兒判斷的結果
lowers = []

for s in L8:
    if s.isupper():
        capitals.append(s)
    if s.islower():
        lowers.append(s)
        
print('全大寫字串有：', capitals)
print('全小寫字串有：', lowers)


# In[16]:


# 不要在對表列進行for迴圈時做任何增減成員的動作
# 因為for迴圈是對表列的每個成員做某些運算，
# 如果你增減成員，會造成問題。

l = 'this is a pen not a book I do not know'.split()

for w in l:
    print(w)
    l.pop(0)         # 每進行一次就刪除位址為0的成員
                     # 結果如下。因為：在進行移除之後，
                     # 下一次詞變成第一個，但第一個已處理過，
                     # 故處理下一個。這就是為什麼結果是跳一個的原因


# ### 上課小練習
# 
# 1. 請用表列列出10個你想去玩的地方的英文地名，並執行：
#     1. 列出這10個地方(以表列形式)
#     1. 反向列出這10個地方
#     1. 由小排到大
#     1. 由大排到小
#     1. 在第一個位置加入Antartic，最後一個位置加入：Arctic See
#     1. 在中央的位置加入Chicago
#     1. 分別刪除第3筆及第9筆資料
# 

# ### 字典 (dictionary)
# 
# - 字典是一種與字串、表列、有序組很不同的資料類型：
#     1. 其成員是 關鍵字(key):值(value) 這種配對的組合，以冒號隔開
#     1. 字典的成員沒有順序，也就是不能以位址(index)及切片來取得其內容
#     1. 如果要取得字典的內容，必須使用關鍵字。
#     1. 長度不限，內容不需具同質性，可以有任意的巢狀包孕(字典的配對組的值可以是字典)
#     1. 字典以大括號標示。
#     1. 同一個字典中，關鍵字只能有一個，值則沒有限制
# - 但是，字典與表列有一點相同處：都可以立刻改變字典的內容 (mutable)
# - mutable vs. immutable
#     1. mutable: 表列、字典
#     1. immutable: 數值(number)、字串、有序組
# - 例如：

# In[17]:


d = {'張三':['經理', 30000, 7], '李四':['組長', 25000, 5], '王五':['業務', 22000, 2], '趙六':['網管', 22000, 1], 
     '孫七':['程式設計師', 27000, 5], '王九': 100, '韋一笑':{'綽號':'青翼蝠王', '職位':'護教法王', '絕技':'輕功'}}
print('1: ', d['李四'])
print('2: ', d['李四'][0])                # 因為值為表列，故可使用indexing來取得表列內容
print('3 (d的長度): ', len(d))
print('4 (王五在不在d中): ', '王五' in d)  # 可以問關鍵字在不在某字典中
print('5 (100在不在d中): ', 100 in d)     # 把 100 當關鍵字看待，故為 False
print('6: ', d['韋一笑']['絕技'])         # 因為"韋一笑"的值又是個字典，故可以再用關鍵字來取得包孕的字典裏的值
d['張三'][1] = 35000                     # 直接改變值(為表列)的內容
print('7: ', d)
d['王九'] = "無名小卒"                    # 直接改變值
print('8: ', d)
del d['王九']                            # 刪除一個配對
print('9: ', d)


# In[19]:


# 以下為字典方法

d1 = {'張三':['經理', 30000, 7], '李四':['組長', 25000, 5], '王五':['業務', 22000, 2], '趙六':['網管', 22000, 1], 
     '孫七':['程式設計師', 27000, 5], '王九': 100, '韋一笑':{'綽號':'青翼蝠王', '職位':'護教法王', '絕技':'輕功'}}

d1.clear()                                          #清空字典內容
print('1: ', d1)

d1 = {'張三':['經理', 30000, 7], '李四':['組長', 25000, 5], '王五':['業務', 22000, 2], '趙六':['網管', 22000, 1], 
     '孫七':['程式設計師', 27000, 5], '王九': 100, '韋一笑':{'綽號':'青翼蝠王', '職位':'護教法王', '絕技':'輕功'}}

d = d1.copy()

print('\n2: ', d)
print('\n3: ', d1.get('韋一笑'))                      # 在沒辦法用方括號來做關鍵字取值時，可以使用
print('\n4: ', d1.get('楊過'))                        # 沒有該關鍵字不會有錯誤訊息(KeyError)，這點很重要

print('\n5: ', d1.items())                           # 取出某字典中所有的配對，以有序組方式呈現
print('\n6: ', d1.keys())                            # 取出某字典中所有的關鍵字，可用list()轉為表列，如果用在for迴圈則直接用字典名稱即可
print('\n6-2: ', d1.values())                        # 取出字典中所有的值，可以list()轉為表列，可直接用在for迴圈中
d1.pop('王九')                                       # 刪除 王九這個配對
print('\n7: ', d1)        
print('\n8: ', d1.pop('楊過', '沒這個關鍵字哦！'))    # 可以指定無關鍵字時的訊息，如不指定，則出現錯誤

d1 = {'張三':['經理', 30000, 7], '李四':['組長', 25000, 5], '王五':['業務', 22000, 2], '趙六':['網管', 22000, 1], 
     '孫七':['程式設計師', 27000, 5], '王九': 100, '韋一笑':{'綽號':'青翼蝠王', '職位':'護教法王', '絕技':'輕功'}}

print('\n9: ', d1.popitem(), d1)                     # 從字典刪除一個配對，無法指定要刪除哪個，回傳一個有序對

d2 = {'John': 45, 'Mary':23, 'Susan':30}

d1.update(d2)
print('\n9: ', d1)                                   # 把d2的內容加入d1

seq = 'Hank', 'Nick', 'Helen', 'Song'                # 一個有序組
d3 = dict.fromkeys(seq)                              # 把seq中的成員當成關鍵字，這是建造一個沒有值的字典，供稍後使用
print('\n10: ', d3)                                   


# ### 幾點注意事項
# 
# 1. 關鍵字：值 配對，不見得兩者要有關係。因為字典很容易從關鍵字找到其值，故，如果你有需要用這種方法來快速從某個值找到另個值的時候，即使這兩個值沒有關係，也可使用字典。
# 1. 在自然語言處理中，字典的常用處之一是：記載詞頻。
# 1. 如果你想從值來找到關鍵字，需要使用for迴圈。
# 1. 要在for迴圈使用關鍵字，僅使用字典；但要使用值，則要用 .values()將值取出。
# 1. 看一下下面的例子：

# In[27]:


tokens = ['taipei', '(', 'taiwan', 'news', ')', '—', 'a', 'new', 'taipei', 'city', 'man', 'surnamed', 'huang', 'faces', 'a', 'nt', '$', '1', 'million', '(', 'us', '$', '33,000', ')', 'fine', 'for', 'patronizing', 'a', 'night', 'club', 'when', 'he', 'was', 'supposed', 'to', 'be', 'at', 'home', 'observing', 'a', '14-day', 'quarantine', '.', 'the', 'new', 'taipei', 'city', 'government', 'said', 'that', 'huang', ',', 'who', 'resides', 'in', 'sanchong', 'district', ',', 'was', 'booked', 'for', 'the', 'quarantine', 'violation', 'by', 'the', 'taipei', 'city', 'police', 'department', 'when', 'they', 'made', 'a', 'spot', 'check', 'at', 'a', 'night', 'club', 'on', 'sunday', 'morning', ',', 'cna', 'reported', '.', 'huang', 'returned', 'to', 'taiwan', 'from', 'southeast', 'asia', 'on', 'march', '18', 'and', 'was', 'supposed', 'to', 'quarantine', 'himself', 'at', 'home', 'until', 'april', '2.', 'the', 'new', 'taipei', 'city', 'department', 'of', 'health', 'said', 'that', 'after', 'receiving', 'the', 'report', 'from', 'the', 'taiwan', 'centers', 'for', 'disease', 'control', ',', 'the', 'department', 'decided', 'that', 'because', 'huang', 'visited', 'a', 'nightclub', ',', 'which', 'is', 'an', 'enclosed', 'space', ',', 'his', 'violation', 'is', 'considered', 'to', 'be', 'especially', 'severe', '.', 'therefore', ',', 'the', 'department', 'is', 'slapping', 'him', 'with', 'a', 'fine', 'of', 'nt', '$', '1', 'million', '.', 'the', 'department', 'urged', 'those', 'under', 'quarantine', 'to', 'keep', 'in', 'mind', 'that', 'fines', 'for', 'violations', 'may', 'range', 'from', 'nt', '$', '100,000', 'to', 'nt', '$', '1', 'million', '.']

print('總共有%i個詞' % len(tokens))
print('='*100)

d = {}                               # 建立一個空字典，等著把詞頻放進去

for t in tokens:                     # tokens裏的每個成員都掃過一次
    if t not in d:                   # 如果詞(t)不在字典d中(=不是d中的關鍵字，沒辦法判斷值在不在哦！)，避免重複計算同一個詞
        d[t] = tokens.count(t)       # 在 d中加入 t:d.count(t)這個配對，也就是 詞:詞出現的次數

# 把 d 的值(=次數)都取出來，用set()去掉重覆的，轉為表列，
# 再由大排至小排序

v_sorted = sorted(set(d.values()), reverse=True)

for v in v_sorted:                  # 這裏示範如何從值去取得該值的關鍵字。對v_sorted(這是排序過的值)從頭到尾掃過一次，
    for k in d:                     # 然後，對 d 中的關鍵字 k 做一掃描，
        if d[k] == v:               # 如果 d[k] = v，也就是 k 這個關鍵字的值(=出現次數) = v
            print(f"{k}出現的次數為：{v}")
            #print('%s 的出現次數為：%i' %(k, v))    # 將之印出


# ## 產生字典的方式
# 
# 1. 如果已經知道 關鍵字:值 配對，可以直接寫入程式碼中。之後可以自由做增刪。
# 1. 如果事前不知道有什麼配對，可以先建立一個空的字典並指派給一個變數，之後可以在程式運行後，將 關鍵字:值 配對加入。
# 1. 如果你有一個新的字典，想加入舊的字典中，可以使用 .update()。
# 1. 如果有兩個有順序的物件，如表列、字串，則可使用：dict(zip(A, B))
# 1. 使用dict keyword-argument form

# In[28]:


a = [1,2,3,4]
b = [5,6,7,8]

print('zip(a, b): ', zip(a,b))
print('d1: ', d1)

s1 = 'this'
s2 = 'THIS'
d2 = dict(zip(s1, s2))
print('d2: ', d2)

d3 = dict(((1, 100), (2, 200), (3, 300)))
print('d3: ', d3)

# dict keyword-argument form

d4 = dict(name='mel', age=45)                     # 關鍵字不能是字串
print('d4: ', d4)
d5 = dict([('name', 'mel'), ('age', 45)])         # 在有序組中關鍵字必須是字串(如果不是數字的話)
print('d5: ', d5)


# #### 課堂小練習
# 
# - 在NLP中，常需要計算標準化詞頻，算法為：$ \frac {詞出現次數} {文本長度}$。利用下面一小篇新聞的斷詞，計算每個詞的標準化詞頻，存入一個叫wordFreq的字典。
# 

# In[39]:


tokens = ['我們', '必須', '正視', '聲量階級', '新貴', '興起', '引發', '的', '社會', '問題', '。', '聲量', '新貴', '是', '新', '的', '社會', '不', '平等', '現象', '。', '透過', '按', '讚數', '、', '追蹤數', '、', '點閱數', '、', '貼文數', '等', '網路聲量', '，', '這些', '新貴', '擁有', '一般', '人', '沒有', '的', '社會', '地位', '，', '也', '享有', '一般', '人', '沒有', '的', '權勢', '。', '\n', '臉書', '是', '縱容', '這些', '權貴', '的', '幫凶', '。', '自', '九月', '十四日', '起', '，', '華爾街', '日報', '以', '「', '臉書文件', '」', '（', 'Facebook', ' ', 'Files', '）', '為', '專題', '，', '刊登', '系列', '九篇', '調查', '報告', '文章', '。', '由於', '其內', '容', '是', '根據', '吹', '哨人', '法蘭西絲', '・豪', '根', '（', 'Frances', ' ', 'Haugen', '）', '提供', '的', '臉書', '內部文件', '資料', '，', '華爾街', '日報', '這', '一', '系', '列報', '導', '，', '向', '外', '界', '揭露', '社群', '媒體', '長久以', '來', '暗黑', '的', '經營', '手法', '，', '同時', '再次', '證明', '臉書', '創辦人', '祖克柏', '一直', '飽', '受', '批判', '的', '為富不仁', '問題', '。', '\n', '\n', '臉書', '為', '權貴', '大', '開特', '權', '後', '門', '，', '正', '是', '華爾街', '日報系', '列報', '導', '第一篇', '文章主題', '。', '臉書', '對', '外', '強調', '，', '只', '要', '使用者', '上傳', '的', '內容', '有', '問題', '，', '它', '就', '會', '依照', '其', '審查', '規定', '刪除', '，', '並且', '給予', '處罰', '。', '然而', '，', '實際', '的', '情況', '真', '是', '如此', '嗎', '？', '\n', '\n', '「', '臉書文件', '」', '報導', '指出', '，', '臉書', '內部', '有', '一份', '名為', '「', '白', '名單', '」', '的', '貴賓清單', '，', '總數', '高達', '五百八十萬', '，', '包括', '川普', '、', '哈', '巴狗道格', '（', 'Doug', ' ', 'the', ' ', 'Pug', '）', '（', '一隻', '有', '五百八十五萬', '追蹤者', '的', '哈', '巴狗', '）', '等', '。', '能夠', '進入', '這個', '「', '白', '名單', '」', '使用者', '，', '往往', '是', '具', '有', '「', '新聞', '價值', '」', '、', '「', '影響力', '」', '、', '「', '受', '歡迎', '」', '、', '「', '（', '對', '臉書', '）', '公', '關', '風險', '」', '等', '條件', '。', '臉書', '特別', '為', '這群', '備', '受', '注目', '的', '使用者', '，', '設立', '一個', '「', '交叉', '檢查', '」', '（', 'cross', ' ', 'check', '或', '是', '所', '謂', '的', 'XCheck', '）', '的', '審查', '機制', '。', '\n', '\n', '原本', '用來', '規範', '內容', '的', '管理', '機制', '，', '反', '而', '變成', '聲量', '新貴', '的', '方便之門', '。', '\n', '\n', '只', '要', '屬於', '「', '白', '名單', '」', '內容', '，', '臉書', '內部', '管理人員', '就', '會', '自動', '睜', '一隻', '眼', '閉', '一隻', '眼', '處理', '他們', '的', '違規', '行為', '，', '甚至', '有', '廿四小時', '的', '通融期', '。', '根據', '華爾街', '日報報導', '，', '這群', '聲量', '新貴', '上傳', '的', '內容', '，', '接受', '審查', '的', '不', '到', '百分之十', '。', '光', '是', '二', '○', '二', '○', '年', '，', '「', '交叉', '檢查', '」', '允許', '破壞', '規定', '內容', '繼續', '留在', '臉書', '，', '直', '到', '觀看', '總數', '達到', '一百六十億次', '後', '，', '這些', '內容', '才', '被', '移除', '。', '\n', '\n', '聲量', '新貴', '寄生', '在', '臉書', '，', '而', '臉書', '需要', '靠', '他們', '賺取', '更大', '的', '營收', '利潤', '。', '這種', '共謀', '關係', '形成', '社群', '媒體', '的', '一種', '病態生態', '。', '尤其臉', '書', '加強', '演算法', '推介', '功能', '的', '運用', '，', '密集', '提供', '同溫層', '的', '訊息', '與', '意見', '，', '此', '一', '病態', '生態', '已', '成為', '人們', '思想言行', '偏', '激化', '、', '兩', '極', '化溫床', '。', '有', '心', '人士', '利用', '傳播', '假', '新聞', '、', '倡議', '反', '科學', '論點', '、', '鼓吹', '仇恨', '意識', '等', '偏', '激手段', '，', '煽動', '社群', '媒體內戰', '，', '讓', '網路聲量', '變成', '是', '自己', '私欲', '的', '利益', '。', '\n', '\n', '「', '臉書文件', '」', '系列', '調查', '報導', '清楚', '顯示', '，', '病態', '社群', '媒體', '的', '關鍵', '課題', '，', '不', '是', '內容', '審查', '，', '而', '是', '落實', '公司', '治理', '以及', '演算法', '規範', '。', '社群', '媒體', '是', '一個', '牽涉', '到', '龐大', '利益', '的', '商業活動', '，', '但', '其', '所', '衍生', '的', '眾多', '社會', '成本', '（', '例如', '霸凌', '、', '孤獨', '等', '）', '卻是', '由', '全民', '所', '負擔', '。', '\n', '\n', '現今', '有', '越來', '越多', '政府', '與', '組織', '積極', '要求', '臉書', '進行', '改革', '，', '台灣', '的', '政府', '並', '沒有', '太多', '作為', '。', '難道', '是', '因為', '政府', '自己', '正', '是', '聲量', '新貴', '的', '受益者', '？']
len(tokens)


# ### 有序組(元組，tuple)
# 
# ## 有序組
# 
# - 有序組，我之所以這樣翻譯tuple，是因為，tuple的成員是有順序的，就跟字串、表列一樣。
# - 有序組以小(圓)括弧標示：(xxx, yyy, zzz, aaa, ...)
# - 有序組跟表列是很類似的：成員有順序、成員不需具同質性、沒有限制成員的個數，等。
# - 但，有序組跟表列有一點很重要的差別：有序組不允許直接改變其內容！！
# - 實務上，如果你有些順序需要注意的資料，但又不想在程式運作過程中資料內容(不小心)被改變，就應該選用有序組；如果在運算過程中，有需要直接改變資料內容，則選用表列。
# 
# ### 有序組的位址與切片
# 
# - 有序組跟字串、表列一樣，都可以使用位址及切片的方式來取得其內容。
# - 例如：

# In[29]:


t = ("張三", "李四", 456, 789, 'this is a tuple', '楊過', '郭靖', '小龍女', '郭襄')
print('len(t): ', len(t))
print('456 in t: ', 456 in t)
print('郭芙 in t:', '郭芙' in t)
print('1: ', t[0])
print('2: ', t[4])
print('3: ', t[3:8])
print('4: ', t[-1])
print('5: ', t[:8:3])
print('6: ', t[5:])
print('7: ', t[-1:3:-2])


# In[30]:


# 有序組的方法只有兩個：count()及index()
# 可能因為：(1) 表列可以代替有序組做到很多事；(2) 有序組不能直接改變內容

t2 = tuple(list('thisisabooknotapenthatisaknifenotabook'))
print('t2: ', t2)
print('='*100)
print('# of k: ', t2.count('k'))
print('index of 1st i: ', t2.index('i'))


# ## 集合 (set)
# 
# - 集合(set) 是Python最後一個儲存資料的物件。
# - 集合有以下特性：
#     1. 集合的成員個數無限定，且不需具同質性
#     1. 集合的成員沒有順序，且是唯一的(重複的成員會被去除)
#     1. 集合可以立刻改變其成員(與表列、字典相同)
#     1. 集合以大括號{}或set()來建立。
#     1. 集合的成員必須是immutable，也就是，集合的成員不能是集合(表列、字典)。
# - 可立刻改變成員(mutable)：表列、字典、集合
# - 不可立刻改變成員(immutable)：數值(number)、字串、有序組

# In[31]:


# 集合就像數學定義一樣，用大括號括起，成員以逗點分隔
# 集合跟字典都用大括號，集合可視是沒有值的字典

ling = {'syntax', 'semantics', 'phonetics', 'phonology', 'computational linguistics'}
print('集合的類型：', type(ling))
mixed = {'syntax', 1234, (55, 66, 77)}
print('成員類型混合的集合：', mixed)

mixed02 = {'syntax', 12, [44,55]}       # 不能有mutable成員，故出現錯誤訊息


# In[32]:


# 集合的操作

ling = {'syntax', 'semantics', 'phonetics', 'phonology', 'computational linguistics', 'corpus linguistics'}
ling2 = {'phonology', 'semantics', 'sociolinguistics', 'pragmatics', 'discourse analysis', 'RST', 'SDRT'}
print('集合成員檢查：', 'phonetics' in ling)
print('集合成員檢查：', 'mathematics' in ling)
print('集合成員檢查：', 'mathematics' not in ling)
print('集合成員個數：', len(ling))
print('交集：', ling & ling2)
print('聯集：', ling | ling2)
print('差集：', ling-ling2)
print('對稱差集：', ling ^ ling2)            # 找出只出現在一個集合的成員


# In[33]:


# 上面的交集等，亦可以集合方法來處理

ling = {'syntax', 'semantics', 'phonetics', 'phonology', 'computational linguistics', 'corpus linguistics'}
print('原來的集合：', ling)
ling.add('MP')
print('增加成員：', ling )
ling_copy = ling.copy()
print('淺層拷貝：', ling_copy)           # 先看一下下面的淺層拷貝的說明
ling.clear()
print('刪除所有成員：', ling)

ling = {'syntax', 'semantics', 'phonetics', 'phonology', 'computational linguistics', 'corpus linguistics'}
print('差集：', ling.difference({'semantics', 'phonology'}))  # 產生新集合，但不影響原集合
ling.difference_update({'semantics', 'phonology'})
print('影響原集合之差集：', ling)        # .difference_update()會直接改變原集合的內容

ling = {'syntax', 'semantics', 'phonetics', 'phonology', 'computational linguistics', 'corpus linguistics'}

ling.discard('corpus linguistics')
print('刪除指定成員：', ling)
print('交集：', ling.intersection({'phonetics', 'semantics', 'Griceanims', 'neo-Griceanism'})) # 產生新的集合
ling.intersection_update({'phonetics', 'semantics', 'Griceanims', 'neo-Griceanism'})
print('影響原集合的交集：', ling)

ling = {'syntax', 'semantics', 'phonetics', 'phonology', 'computational linguistics', 'corpus linguistics'}

print(ling.isdisjoint({1,2,3}))                  # 判斷與另一個集合是否完全沒有交集
print({'syntax', 'semantics'}.issubset(ling))    # 檢查是否為子集合
print(ling.issuperset({'phonology', 'computational linguistics'}))   # 檢查是否為超集合

print(ling.pop())                                # 任意移除一個成員，回傳被移除的成員
ling.remove('corpus linguistics')
print('移除指定的成員：', ling)

print({1,2,3,4,5,6}.symmetric_difference({4,5,6,7,8,9}))
nSet = {1,2,3,4,5,6}
nSet.symmetric_difference_update({4,5,6,7,8,9})
print('影響原集合的對稱差集：', nSet)
print('聯集：', {1,2,3,4}.union({3,4,5,6}))
nSet.update({'John', 'Mary', 'Sue'})
print('把新集合的成員加入原集合中：', nSet)


# ### if 敍述 (if statement)
# 
# - if 敍述的基本語法如下： <br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊01<br>
# &emsp;else:<br>
# &emsp;&emsp;&emsp;程式碼區塊02
# 
# - if 敍述的執行流程為：<br>
# &emsp;檢查if標示的條件是否吻合：<br>
# &emsp;&emsp;(1)如果吻合，則執行程式碼區塊01<br>
# &emsp;&emsp;(2)如果不吻合，則執行程式碼區塊02<br>
# &emsp;&emsp;(3)如果在if...else...之後還有程式碼，則在執行區塊01或02之後，會繼續執行if...else...之後的程式碼。
# 
# - 例如：

# In[41]:


age = 18

if age> 20:
    print('你可以買酒！')
else:
    print('你不能買酒！')


# - if 敍述可以只有if的部份，而沒有else。
# - if 敍述可有有很多個 if，但如果有else，則只能有一個。
# - 第二個以後的if有兩種：
#     1. if：不具排他性
#     1. elif (= else if)：具排他性，也就是，只要某個if的條件符合，其他if都不再嘗試。
# - 語法如下：<br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊01<br>
# &emsp;elif 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊1-1<br>
# &emsp;elif 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊1-2<br>
# &emsp;elif 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊1-3<br>
# &emsp;... <br>
# &emsp;else:<br>
# &emsp;&emsp;&emsp;程式碼區塊02<br>
# <br><br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊01<br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊1-1<br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊1-2<br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;程式碼區塊1-3<br>
# &emsp;... <br>
# &emsp;else:<br>
# &emsp;&emsp;&emsp;程式碼區塊02<br>
# 

# In[42]:


a = 105

if a%3 == 0:
    print('a 是3的倍數')
if a%5 == 0:
    print('a 是5的倍數')              # 用 if，因為兩個條件都符合，故兩個區塊都執行
else:
    print('a既不是3的倍數也不是5的倍數')


# In[43]:


a = 105

if a%3 == 0:
    print('a 是3的倍數')
elif a%5 == 0:
    print('a 是5的倍數')             # 用 elif，具排他性，只會執行第一個符合的 if 條件，其他不執行
else:
    print('a既不是3的倍數也不是5的倍數')


# In[44]:


# 如果 if 的條件都不符合，那麼，使用 if 或 elif 都沒有差別。

a = 103

if a%3 == 0:
    print('a 是3的倍數')
if a%5 == 0:
    print('a 是5的倍數')
else:
    print('a既不是3的倍數也不是5的倍數')


# ### 一些注意事項
# 
# 1. if/elif/else 之後，一定要有個冒號！
# 1. 冒號之後，要換行，換行後的程式碼區塊一定要內縮！注意：只能用空白鍵內縮，而不是tab鍵！(有的純文字編輯器會判斷並自動內縮。)
# 1. if/elif/else的程式區塊，可以再用if敍述。沒有規定可以放幾層，但是，實務上，太多包孕的if敍述，會讓程式設計師邏輯判斷難以進行(對Python本身倒是沒有影響)。
# 1. 如果有多層包孕的if敍述，記得要層層內縮！如：<br>
# &emsp;if 條件：<br>
# &emsp;&emsp;&emsp;if 條件：<br>
# &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;程式碼區塊01<br>
# &emsp;else:<br>
# &emsp;&emsp;&emsp;程式碼區塊02

# ### 課堂練習
# 
# 1. 請設計一個程式，執行下面三個工作。
#     1. 若輸入是小寫字元，改成大寫
#     1. 若輸入是大寫字元，改成小寫
#     1. 若是阿拉伯數字，照舊輸出
#     1. 其他的，輸出錯誤
#     
# 1. 有一個百貨公司五十週年週年慶。消費滿10萬元，打九折；8萬，打95折；5萬，打98折。如果消費恰好五十歲，則不論金額，都打95折。請設計這個程式。

# ## 迴圈(loops)
# 
# - 迴圈的功能是，重覆地執行某些運作。
# - Python中的迴圈有兩種：while迴圈及for迴圈。
#     1. while迴圈是在符合某些條件的情況下，重覆某些運算。
#     1. for迴圈是對某個具多重成員的物件，對其成員做某些重覆運算。
# 
# ### while 迴圈
# 
# - 格式：<br>
# &emsp;&emsp;while 條件:<br>
# &emsp;&emsp;&emsp;&emsp;執行要做的運算<br>
# &emsp;&emsp;else:<br>
# &emsp;&emsp;&emsp;&emsp;條件不符時要做的運算<br>
# 
# - else 的部份可有可無。常常看到的while 迴圈，是沒有else的部份的。
# - 使用while迴圈，要注意一點：條件必要在某個時候轉為假，否則，迴圈會變成無限迴圈，一直執行下去。
# - 如：<br>
# &emsp;&emsp;while True: <br>
# &emsp;&emsp;&emsp;&emsp;print('Type crtl+c to stop me!)<br><br>
# &emsp;就是一個無限迴圈，因為True永遠不會變假，故條件永遠為真。

# In[45]:


x = 'spam'

while x:                                 # 非空串即為真，空字串則為假
    print(x, end=' ')
    x=x[1:]     


# In[46]:


a = 0
b = 10

while a<b:
    print(a, end=' ')
    a += 1                              # 每執行一次，a就加一，等a不再小於10，也就是a=10時，while條件轉為假，迴圈停止。


# ### 可以接在 while 之後的成份
# 
# 1. break：如果條件吻合，中斷迴圈
# 1. continue：回到最近的迴圈第一行，開始執行
# 1. pass：什麼都不做
# 1. else: while迴圈條件不符時，且未被中止(break)時執行
# 
# - 格式：<br>
# &emsp;&emsp;while 條件:<br>
# &emsp;&emsp;&emsp;&emsp;要執行的運算<br>
# &emsp;&emsp;&emsp;&emsp;if 條件2: break<br>
# &emsp;&emsp;&emsp;&emsp;if 條件3: continue<br>
# &emsp;&emsp;else:<br>
# &emsp;&emsp;&emsp;&emsp;要執行的運算 <br>

# In[47]:


x = 10
while x:
    x -= 1
    if x%2 != 0: continue                   # x不能整除2時，跳回迴圈第一行；可以整除時，才執行print()
    print(x, end=' ')

print('\n')

y = 10
while y:
    y -= 1
    if y%2 != 0:                           # 沒有continue，則直接執行print() 
        print(y, end=' ')

print('\n')

z = 10
while z:
    z -= 1
    if z%2 == 0:                          # 不能整除2時，回到迴圈開始再重頭來 = 能整除2時，執行print()
        print(z, end=' ')
        
print('\n')

zz = 10
while zz:
    if zz % 4 == 0: break                # zz能整除4時，中止；否則，執行其下兩行
    print(zz)    
    zz -= 1
    
while True:
    name = input('Enter name:')
    if name == 'stop': break            # 也可以用來利用輸入的字串來做為中止while迴圈
    age = input('Enter age:')
    print('Hello, %s => %i' %(name, int(age)**2))


# In[ ]:


# 一個用處比較明顯的例子

import random

names = ['郭襄', '郭芙', '公孫綠萼', '程英', '陸無雙', '完顏萍', '小龍女']

pickedName = random.choice(names)

count = 5

while count > 0:
    print('猜猜看我想到的神鵰俠侶中的俠女是誰？')
    print('你有%i次機會。' %count)
    guess = input('我的答案是：')
    count -= 1
    if guess == pickedName:
        print('猜對了！你好棒！')
        break                                 # 猜對了，中止迴圈
    else:
        print('不對哦！\n')                    # 沒猜對，又不到五次，繼續猜
else:
    print('你五次都猜錯了...')                 # 沒猜對，又已猜過五次，執行本行


# - 注意：while迴圈有沒有else，其運作不同：
#     1. 有else：要while的條件為假時，才會執行else以下的程式碼。<br>
#     &emsp;&emsp;&emsp;&emsp;while 條件:<br>
#     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;運算一<br>
#     &emsp;&emsp;&emsp;&emsp;else:<br>
#     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;運算二<br>
#     1. 沒有else時，不管while條件為真為假，只要離開while迴圈，就會執行。<br>
#     &emsp;&emsp;&emsp;&emsp;while 條件:<br>
#     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;運算一<br>
#     &emsp;&emsp;&emsp;&emsp;運算二<br>

# ## for 迴圈
# 
# - for 迴圈運作於包含成員的物件，如，字串、表列、字典、有序對等，對該物件的每個成員做運算。
# - 格式一：<br>
# &emsp; &emsp; for 變數 in 包含內部成員的物件：<br>
# &emsp; &emsp;&emsp; &emsp;要執行的運算一<br>
# &emsp; &emsp;else:<br>
# &emsp; &emsp;&emsp; &emsp;要執行的運算二<br>
# - 格式二：<br>
# &emsp; &emsp; for 變數 in 包含內部成員的物件：<br>
# &emsp; &emsp;&emsp; &emsp;要執行的運算一<br>
# &emsp; &emsp;&emsp; &emsp;if 條件1: break<br>
# &emsp; &emsp;&emsp; &emsp;if 條件2: continue<br>
# &emsp; &emsp;else:<br>
# &emsp; &emsp;&emsp; &emsp;要執行的運算二<br>
# - 請注意：
#     1. else的部份，跟while迴圈一樣，是可有可無的。
#     1. 雖然格式二中的if條件只執行break/continue，但實際上，for迴圈中的if條件可以正常使用，不限於break/continue。
#     1. while迴圈、for迴圈及if條件，可以互相包孕，理論上沒有層數的限制。唯一的限制是：程式設計師要能夠釐清使用的邏輯。

# In[49]:


s = 'A push by the US State Department to include the phrase "Wuhan virus" in a joint statement with other Group of Seven members following a meeting of foreign ministers on coronavirus on Wednesday was rejected, resulting in separate statements and division in the group.'
for c in s:                                       # 注意：字串的基本單位是字元(character)
    print('%s => %i' %(c, ord(c)))


# In[50]:


words = s.split()

longWs = []
shortWs = []

for w in words:                                # 表列(有序組)基本單位是以逗點隔開的成員
    if len(w) > 5:
        longWs.append(w)
    else:
        shortWs.append(w)
print('longWs:', longWs)
print('shortWs:', shortWs)


# In[51]:


names = ['張無忌', '胡斐', '阿朱', '王語嫣', '霍青桐', '朱九真']
books = ['倚天屠龍記', '飛狐外傳', '天龍八部', '天龍八部', '書劍恩仇錄', '倚天屠龍記']

d = dict(zip(names, books))

for key in d:                           # 字典的基本單位是關鍵字
    print('%s 出現於 %s 一書中' %(key, d[key]))
    
# 以下可以達到相同效果
print('='*50)

for key, val in d.items():              # 使用 .items() 把 關鍵字:值 配對以有序組的程式取出
    print('%s 出現於 %s 一書中' %(key, val))


# In[71]:


# 數字相加

res = 0

for i in range(1, 101):
    res += i            # res = res + i
    
print(res)


# #### 上課小練習
# 
# - 上面做過的簡單MLU練習：假設你收集到一個小baby說的六個句子：up、come up、play ball、come play ball、daddy come play ball、daddy play ball、daddy play too。你想要計算一下這個baby的 MLU (Mean Length of Utterance)。你應該怎麼做？(使用下面Excercise 1的部份程式碼)
#     1. 如果你的MLU要取到小數點下兩位，四捨五入，該怎麼做？
#     2. 如果你的MLU要小數點下無條件捨去，該怎麼做？
# - 怎麼樣for迴圈以及前面學到的技術來計算這個問題？

# ## 載入 (import)
# 
# - Python內建了許多模組(module)可以在需要時載入，如math、decimal、random等等
# - Python受人歡迎的原因之一是，有許多人替其開發模組套件，可以供人使用，如NLTK(自然語言處理工具組)、numpy(計算arrays)、pandas(與Excel功能相似)、matplotlib (繪製圖表)等等。
#     1. 這些非內建模組套件需要自行下載安裝，需要的，請自行搜尋其下載方式。
# - 這些不是打開Python就載內的模組套件，都需要載入(import)
# - 格式：
#     1. import 模組   (載入整個模組)
#     1. import 模組 as 較短的名稱
#     1. from 模組 import 函式1, 函式2, .... (自模組載入(只有)函式1, 函式2, ...)
#     1. from 模組 import 函式 as 較短的名稱

# In[52]:


import math

math.sqrt(100)                          # 只載入math模組，要使用其包含的函式，需要用：模組.函式()


# In[53]:


from math import factorial

factorial(5)                            # 從模組載入特定函式，可以僅使用該函式


# In[54]:


from math import factorial as fr        # 覺得函式太長，可以用 as 縮寫之

fr(5)


# In[55]:


import numpy as np

grades = [45, 76, 88, 54, 99, 87, 45, 46, 75, 74]
print('平均：', np.mean(grades))
print('標準差：', round(np.std(grades), 2))
print('變異數：', round(np.var(grades), 2))


# ### 注意事項
# 
# - 要使用 import 來載入模組，該模組要在適當的路徑上，如果是內建的模組，則不用擔心；如果是需要下載安裝的模組，最好去查閱該模組的使用說明(documentation)，看看如何安裝。最常見的是使用：pip 安裝。pip安裝，需要在提示字元(DOS模式下執行)，由於這又牽涉到DOS路徑的設定，最簡單的方式是，使用 anaconda (powershell) prompt，在這個環境下，路徑都已設定完成，只要直接使用 pip 即可。
# - 模組聽起來是個很嚴肅的名詞，但是，Python 模組其實就是一個 .py 檔，就跟你寫的程式一樣。要注意的是，Python模組裏定義了要給人使用的函式(下半部要談的主題)或變數。要使用你自己寫的模組，要import成功，檔案位置很重要：
#     1. 把你自己寫的模組放在跟要用這個模組的程式相同的目錄下，這樣，就可以使用上面的方式來載入。
#     1. 如果你開發較大的專題，會希望把同一個專題的模組放在相同的目錄，不跟其他混在一起。在這種時候，你要在 Python 的目錄下，加入一個叫：dirs.pth的檔案，裏面把你想要 Python 搜尋的目錄列出。 

# # 函式 (function)
# 
# - 函式是一個很重要的議題，學習程式的人都必須學會。
# - 函式的功能是：把一些可能重覆出現的程式碼，集合起來，取一個名字。因為程式碼如果要用很多次，每次都要重覆鍵入，這樣不僅費時，而且輸入多次，犯錯的機會就提高。更重要的是：重覆的事，交給程式來做，就跟迴圈一樣，這才是程式的精義之一！
# - 根據 Learning Python這本書，函式主要好處是：
#     1. 讓程式碼再利用性最大化
#     1. 讓程式碼重覆性最小化
# - 格式：<br>
# &emsp;&emsp;def 函式名稱(論元1, 論元2, ...):<br>
# &emsp;&emsp;&emsp;&emsp;程式內容1<br>
# &emsp;&emsp;&emsp;&emsp;程式內容2<br>
# &emsp;&emsp;&emsp;&emsp;....<br>
# - 例如：

# In[57]:


article = '美中兩強領導人視訊高峰會甫告落幕，各方就傳出美國有意抵制北京冬季奧運訊息，但政治是要講究時機與節奏，就目前端出抵制北京冬奧所能產生各項效應來說，其實相關有利時間節點早就過去，而且展望可能效應亦相當有限，華盛頓決策謀士若是不能深思熟慮，到最後很有可能會弄巧成拙。首先必須指出，在國際社會若要運用抵制運動賽事，作為政治表態與殺傷對方國際形象手段，甚至是存心要在實質商業利益上攪局，必須師出有名才能夠煽動人心獲得響應。因此如何運用特定時間節點，在國際社會對運動賽事東道主，在國際事務上負面行為記憶猶新時斷然出招，才能夠鼓動風潮招朋引伴形成氣勢。儘管國際社會每個成員都會唱政治莫要干預體育高調，尤其是強權更是滿嘴仁義道德，幹起事來卻是凶狠毒辣毫無顧忌。不過若真要抵制運動賽事時，基本上具有三個面向可以當成打擊目標；其中包括選手不參加賽事，企業不捧場媒體不轉播以及政要不出席，以便杯葛東道主運動賽事外交。就目前來說，各方要在明年二月參加北京冬奧，或是三月北京冬季帕奧選手，早就蓄勢待發等待出場競技，此時若是突然叫停，不但對選手準備賽事來說，此種干擾作梗會讓其失望憤怒；許多選手還與商業機構簽有代言商品契約，相關廠商贊助或是實質收益自然就會受到衝擊，許多選手還期待透過競技奪牌，奠定轉戰其他職業表演舞臺，透過賽事成績成為開創後續事業跳板。假若政府到此時輕舉妄動，臨時神來一筆，將攸關重大利益者無端開罪，絕對就是在生產政治票房毒藥。其次就支持賽事藉由贊助活動捐輸經費，以便獲得在賽事現場進行廣告宣傳之企業來說，此時政治攪局必然會減損廣告傳播效應，對於掏出大把銀兩，寄望配合賽事進行廣告宣傳者來說，必然會咬牙切齒，對於突然攪局倡議抵制者來說，事後必然會抱持負面態度，政治獻金或是選舉贊助，這些企業金主都會記在心裡，政治人物看看賽事贊助，要是還不識相，體會不出此事敏感程度，恐怕會被人譏笑為政治外行。再者就要想到專門轉播運動賽事，以便從中獲取商業利益之媒體業者，再加上依附在此產業鏈相關評論分析專家，還有配合賽事轉播進場之廣告商與企業組織，此種關係綿密結構複雜之利益網路，政治人物都要忌憚三分，所以如今箭在弦上，若要抵制杯葛又不事先早點明講，等到萬事就緒再出面攪局，豈不就是自討沒趣？至於各國政要配合出席運動賽事開幕與閉幕典禮，順道進行運動外交高峰會談，早就因為疫情影響，各國高層都不願承擔此種風險，因此，此時聲稱所謂「政治杯葛」，將焦點集中在不出席盛會，其實根本就無法產生具體影響。多個運動賽事政要出席致賀，早就是透過網際網路遠距傳送聲光影像，因此就算端出個理由，聲稱杯葛出席來表達政治姿態，恐怕媒體效應更是無足輕重。美國若是真有心抵制杯葛北京冬奧，就必須及早表態，如今在視訊峰會剛過，突然開始釋放消息，但只是聲稱在考慮抵制，卻未能提出肯定訊息；講實在話，這就是在釋放政治氣球，看看是否有國家願意跟進扈從，否則貿然宣布抵制杯葛，但卻沒有其他國家跟進時，搞到千山我獨行無人相送陪伴，這種淒涼景況豈不是弄巧成拙，擺明讓自己難看嗎？所以美國抵制北京冬奧，不但難有實效風險亦高。冬季奧運其實向來被國際社會譏為有錢人賽事，對於奧運組織成員國來說，能否在冬季奧運闖出一片天，不但受限於氣候條件，相關場地、設施、器具以及訓練過程，就經費預算來說，門檻相對較高。所以能夠主辦冬季奧運，不但本身在相關賽事項目上要有實力奪牌，能夠滿足賽事場地與設施規格，其實亦是國家富強指標，暗示東道主總算擠進國際社會富裕階層行列。所以西方社會某些人士刻意要抵制杯葛北京冬奧賽事，在相當程度上是具有嫌貧愛富地位歧視因素，但此種醜陋心態確實是不能放在檯面，所以當眼睜睜看到中國大陸獲得主辦冬季奧運機會，其實就是對其社會富裕程度加冕認證，此種難以啟口內心酸葡萄不痛快感覺，或許才是西方社會某些人士倡議抵制北京冬奧，但卻又羞於啟口之真正原因吧！'

# 兩個漢字一組

bigrams = []
for i in range(len(article)):
    bigrams.append(article[i:i+2])
    
trigrams = []
for i in range(len(article)):
    trigrams.append(article[i:i+3])
    
quadrigrams = []
for i in range(len(article)):
    quadrigrams.append(article[i:i+4])
    
print(f"bigrams:\n{bigrams}")
print()
print(f"trigrams:\n{trigrams}")
print()
print(f"quadrigrams:\n{quadrigrams}")


# In[58]:


# 以上三組程式，可以把字串兩個字元(三個、四個、五個...) 為一組提取出來。
# 但是，其實這些程式內容除了要提取的字元數不同外，其他的其實是一樣的。
# 所以，我們整合為一個：

def nElem(seq, n):
    '''
    takes two arguments: a sequence and a number n
    returns nGrams of the sequence
    '''
    res = []
    for i in range(len(seq)-(n-1)):
        res.append(seq[i:i+n])
    return res


# In[60]:


print(nElem(article, 2))


# In[62]:


print(nElem(article, 3))


# In[63]:


print(nElem(article, 4))


# ### 說明
# 
# - def 是Python的保留字元，是define(定義)的縮寫。注意！在Python中不能用define！
# - 與迴圈相同，定義函式的名稱及論元之後，需要一個冒號。
# - 冒號下面的程式碼，稱之為本體(body)，要內縮，一直到整個函式結束為止。
# - 函式的本體，可以是任何的Python程式，包括迴圈、條件檢測。只是要記得，函式本體已經內縮了，如果遇到迴圈、條件檢測的本體(冒號之後、換行的程式內容)要進一步的內縮。
# - 上面的nElem()本體中的 return，其作用是把程式本體計算結果回傳出來。在Python解譯器中，執行nElem()，會直接把值印在螢幕上。在Jupyter Notebook上則需要使用print()。但是，如果只是把結果印在螢幕上，其實直接在函式中使用print()就好了。return最重要的功能，其實是，可以把函式運算出來的值，指派給變數，供其他程式使用！

# In[64]:


# print() 函式執行結果

def nElem02(seq, n):
    '''
    takes two arguments: a sequence and a number n
    returns nGrams of the sequence
    '''
    res = []
    for i in range(len(seq)-(n-1)):
        res.append(seq[i:i+n])
    print(res)


# In[65]:


nElem02(article, 2)


# In[68]:


from collections import Counter

bigramFreq01 = Counter(nElem(article, 2))
print('-'*50)
bigramFreq02 = Counter(nElem02(article, 2))
print('-'*50)
print(f"bigramFreq01:\n{bigramFreq01}")
print('-'*50)
print(f"bigramFreq02:\n{bigramFreq02}")


# #### 定義一個可以接受任意個數的論元的函式
# 
# - 上面我們的小練習中有一個計算MLU的簡單程式。
# - 但是，隨著我們收集到的utterances越多，就得重覆執行上面練習中的程式。
# - 我們可以把這個計算MLU的程式寫成函式，並且允許其接受任意個數的論元。

# In[74]:


def mlu(*utterances):
    '''
    takes any number of lists of utterances
    returns MLU (Mean Length of Utterance)
    '''
    mlu = 0
    
    for u in utterances:
        mlu += len(u)
        
    return mlu/len(utterances)


# In[77]:


mlu('daddy come'.split(), 
    'baby eat'.split(), 
    'baby play ball'.split(), 
    'daday give hug'.split(), 
    'babay give dady ball'.split(),
    'mommy drink coke'.split(),
    'mommy put cloth'.split()
   )


# In[78]:


mlu = mlu('daddy come'.split(), 
          'baby eat'.split(), 
          'baby play ball'.split(), 
          'daday give hug'.split(), 
          'babay give dady ball'.split(),
          'mommy drink coke'.split(),
          'mommy put cloth'.split()
         )

print(round(mlu, 4))


# In[76]:


# 來看一下，*args 在Python中以什麼格式出現

def func03(*args): print(args)
    
func03('a', 123, [5,6,7], (8,9,10))


# ## 中文斷詞
# 
# - 斷詞(tokenization或segmentation)是做中文處理的第一步，斷詞也是有相當複雜的任務。
# - Python開源的中文斷詞程式庫 jieba，大概是最多人使用的中文斷詞程式庫了(可能是因為開源=免費？)，不過，jieba主要是利用大陸的語料來訓練的，應用在繁體/正體中文，出錯機會大。
# - 在githup上可以找到幾個利用繁體語料訓練的jieba，如：https://github.com/APCLab/jieba-tw
#     1. 要安裝這個版本的jieba，要先安裝git：https://git-scm.com/downloads (下載適合你的版本並安裝)
#     1. 再以：pip install git+https://github.com/APCLab/jieba-tw.git 來安裝這個版本的jieba
# - 另外，建立漢語語料庫驅，中央研究院中文詞知識庫小組(簡稱：詞庫小組或CKIP)，開發中文斷詞系統也有很長的歷史了，而且，正確率不錯。最近幾年，CKIP Tagger 也有Python的程式庫API了(https://github.com/ckiplab/ckiptagger):
# - 要使用ckiptagger需要在你的虛擬環境中執行下面動作：
#     1. pip install tensorflow
#     1. pip install ckiptagger
#     1. pip install gdown
#     1. 進入你的Python直譯器，如Jupyter Notebook或打開Spyder
#     1. 在Python Console執行：
#         1. from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
#         1. data_utils.download_data_gdown("./")  \[下載資料集，如詞類、斷詞原則什麼的\]
#             - 註：因為我們使用jupyter notebook的方式，是把目錄指向你儲存你的程式的目錄下，故，使用這種方式下載ckiptagger的資料，會到你的工作目錄去。記得，把下載的 data.zip (壓縮檔) 複製到你安裝ckiptagger的虛擬環境的目錄去，比如，我的ckiptagger是在放ckiptagger這個虛擬環境中，就得把這個壓縮檔複製進"C:\\Users\\Admin\\anaconda3\\envs\\ckiptagger"這個目錄之下。
#             - 而且，如果要使用ckiptagger，就必須啟動這個虛擬環境。
#         1. ws = WS("./data")
#         1. pos = POS("./data")
#         1. ner = NER("./data")
#             - 註：在 ckiptagger的原始文件中，使用 ws = WS("./data")來標示ckiptagger的資料庫內容的所在目錄(=工作目錄)；但，我們使用 jupyter notebook 方式，工作目錄是我們儲存 .ipynb 的目錄，故，需要指定ckiptagger 的目錄，放在WS/POS/NER的論元中，也就是：ckiptagger_pth = "C:\\Users\\Admin\\anaconda3\\envs\\ckiptagger"
#        
#             

# In[38]:


from ckiptagger import WS

ckiptagger_pth = "C:\\Users\\Admin\\anaconda3\\envs\\ckiptagger"   #家裏筆電
ws = WS(f"{ckiptagger_pth}/data")

sentence_list = [
    "傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。",
    "美國參議院針對今天總統布什所提名的勞工部長趙小蘭展開認可聽證會，預料她將會很順利通過參議院支持，成為該國有史以來第一位的華裔女性內閣成員。",
    "",
    "土地公有政策?？還是土地婆有政策。.",
    "… 你確定嗎… 不要再騙了……",
    "最多容納59,000個人,或5.9萬人,再多就不行了.這是環評的結論.",
    "科長說:1,坪數對人數為1:3。2,可以再增加。",
]

word_sentence_list = ws(sentence_list)


# In[40]:


for l in word_sentence_list:
    print(l)


# ## 正則表達式 (reqular expression)
# 
# - 正則表達式本來是一種描述形式語言(formal language)的語法規則。
# - 正則表達式所描述的語言稱為：正則語言 (regular language)。
# - 正則語言定義如下：
#     1. 字母集中的每一個字母，都是一個正則語言。
#     1. 正則語言以前後相連(concantenation)、重覆零次或以上 (*)、重覆一次或以上(+)仍是正則語言。
#     1. 正則語言以交集、聯集、補集運作後的結果，仍是正則語言。
# - 假設我們有字母集如下 {a, b}：
#     1. a及b都是正則語言
#     1. a*、a+、b*、b+、a*b+、b+a+，等等，都是正則語言
#     1. a*b* (= a*與b*的聯集) 是一個正則語言
#     1. ....
# - 上面的假設中，用來描述各個正則語言的語法規則就是正則表達式。
# - 在CS的世界中，一般聽到正則表達式，立刻想到的是字串搜尋。
# - 也就是說，正則表達式被用來標明要搜的字串類型，可以用簡單的表達式來搜尋相對複雜的字串。
# - Python包含一個內建的模組 re，可以用來依正則表達式做字串的處理(不只是搜尋)。

# ## 正則表達式的特殊字元
# 
# <img src="Topic08_REImage01.png">
# <img src="Topic08_REImage02.png">

# - 所以，我國的手機格式，可以用正則表達式寫為：'\\d{4}-\\d{6}' 或 r'\d{4}-\d{6}'
# 
# - 格式：<br>
# import re <br>
# 變數 = re.方法(正則表達式, 要在其間搜尋的字串 \[,flags\])
# - 如果擔心特殊字元，可以在前兩個論元(皆為字串)前加上 r <br>
# <br>
# - flags有下面幾種：
#     1. re.I 或 re.IGNORECASE 代表大小寫不分，都是搜尋的目標
#     1. re.DOTALL 代表如果你想要找到的字串跨行也要找到，需要標示此：忽略換行符號 的旗標
#     1. re.VERBOSE 允許你在論元位置標明正則表達式時，加上註解，讓正則表達式想找到對象能更清楚表示
#     1. 旗標是可選擇的，也就是說，可以不用....
#    

# In[79]:


import re

pattern = r'[a-zA-Z]+'                           #任何出現一次及以上的大小寫並全為字母的字元 
m = re.match(pattern, 'tem12po')           
print(1, m.group())                              # .group() 找出符合指定模式的字串
m2 = re.match(pattern, '123Jack00')              # 要搜尋的字串第一個並非字母，搜尋停止，故傳回None
print(2, m2)                                     # 沒找到，用.group()會有出現錯誤訊息


# In[81]:


#import re

pattern = r'[0-9]+'
pattern2 = '[0-9].+'
pattern3 = '[0-9][0-9+]'

m3 = re.search(pattern, 'tem12po')
m4 = re.search(pattern, '123Jack00')

str5 = '''1
45Jack
你好03'''

m5 = re.search(pattern, str5)
m6 = re.search(pattern2, str5, re.DOTALL)  # 要找一個數字其後跟著一個以上的任何字元，下了 re.DOTALL之後，可以換行
m61 = re.search(pattern2, str5)            # 這是pattern2，數字後有接任何字元，因為沒有re.DOTALL，故第一行的1不算
m7 = re.search(pattern3, str5, re.DOTALL)   
m8 = re.search(pattern3, str5)

print('a.', m3.group())
print('b.', m4.group())
print('c.', m5.group())
print('d.', m6.group())
print('e.', m61.group())
print('f.', m7.group())
print(f"g. {m8.group()}")


# In[12]:


# 使用 re 做文本內容蒐尋

import os
import re

curr_pth = os.getcwd()

with open(f"{curr_pth}/data/2MNewsDataSegmented.txt", 'r', encoding='utf8') as f:
    texts = f.read()
    
front = "."*50
back  = "."*50
kw    = "肺炎.{0,5}疫苗"

pattern = f"{front}{kw}{back}"

res = re.findall(pattern, texts)

print(f"找到的例子有：{len(res)}句")
print()

for entry in res:
    print(entry)
    print()


# In[9]:


front = "."*50
back  = "."*50
kw    = "肺炎.疫苗"

pattern = f"{front}{kw}{back}"

res = re.findall(pattern, texts)
print(len(res))

# 跟上面的比，少了第二個例子：新冠肺炎  的  疫苗


# In[18]:


front = "."*50
back  = "."*50
kw    = "機車.{0,30}車禍"

pattern = f"{front}{kw}{back}"

res = re.findall(pattern, texts)
print(len(res))
print()
for entry in res:
    print(entry)
    print()


# ### 文件(情感/分類)分析步驟
# 
# 1. 蒐集文本
# 1. 將文本斷詞
# 1. 將文本數據化，可使用Bag of Words (BOW)、TF-IDF、Word2Vec等。
# 1. 將文本加註標籤
# 1. 將文本拆為訓練集及測試集(有更精細的拆分方法)
# 1. 將訓練集送入演算法中訓練
# 1. 使用測試集做正確率的測驗

# In[23]:


# 網路評語情感分析

#import os
#curr_pth = os.getcwd()

# 原來的檔案是 list of lists of tokens
# 先組合成 list of tokens

with open(f"{curr_pth}/data/posCommentsTokensList.txt", 'r', encoding='utf8') as f:
    ListsTokens = eval(f.read())
    
posTokens = []
for l in ListsTokens:
    posTokens.append(' '.join(l))
    
print(f"正面評語共有：{len(posTokens)}")

with open(f"{curr_pth}/data/negCommentsTokensList.txt", 'r', encoding='utf8') as f:
    ListsTokens = eval(f.read())
    
negTokens=[]
for l in ListsTokens:
    negTokens.append(' '.join(l))
    
print(f"負面評語共有：{len(negTokens)}")


# In[29]:


# 建立 BOW
from sklearn.feature_extraction.text import CountVectorizer

# 先把斷好詞的文本，依原來順序合併成一個表列

allTexts = posTokens + negTokens

BOW = CountVectorizer().fit_transform(allTexts)
BOW = BOW.toarray()


# In[32]:


# 依評論順序加入正面、負面標籤，1=正面，0=負面

labels = [1]*1546 + [0]*1477


# In[36]:


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB 
from sklearn.metrics import accuracy_score

# 將語料分為訓練集、測試集：X 為斷好詞的評語
# y 為情感標籤，測試集的大約為所有文本篇數的 0.2 
X_train, X_test, y_train, y_test = train_test_split(BOW, labels, test_size=0.2)

nb = MultinomialNB()

# .fit() 訓練模型
model = nb.fit(X_train, y_train)

# .predict()對測試集(或新語料)做預測
y_pred = model.predict(X_test)

print(f"accuracy:{accuracy_score(y_test, y_pred)}")


# In[ ]:




