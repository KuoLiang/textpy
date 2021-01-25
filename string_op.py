import re #regulare expression
print "hello"
mystring = "你好 我好 天氣好 abc abcd ABC ABCD 123 1234"
str_new=mystring.replace("你","我")
str_list=mystring.split()

pattern = re.compile(r'.') #find all char but \n
re.findall(pattern,mystring)

pattern2 = re.compile(r'[abc]')
re.findall(pattern2,mystring)

pattern3 = re.compile(r'[a-z]')
re.findall(pattern3,mystring)

pattern4 = re.compile(r'[a-z0-9]') #a to z OR 0-9 ,中文就不合
re.findall(pattern4,mystring)

pattern5 = re.compile(r'[^a-z0-9]') #not a to z OR 0-9
re.findall(pattern5,mystring)

pattern6 = re.compile(r'[a-zA-Z][0-9]') #not a to z OR 0-9
re.findall(pattern6,mystring)
