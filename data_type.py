""" 
Kuo-Liang Ou
kloutw@gmail.com

"""
a = "1"
b = 2**3
c = 20.12545
#c = a+b
print(type(a))
print(type(b))
print(c//b)

#d = input("Your name")
#print("Your name is", d , "!")
print("The answer is %s and %d" %(a,b))
print("The answer is {} and {}".format(a,b))
print("The answer is \n{0} and {1:7.2f}".format(a,c)) #第二個參數共佔七格，取小數第二位四捨五入