def names(pikachu,*args):
    print(pikachu,args)

names("jack",4,"rose",'at',"titanic")
#jack (4, 'rose', 'at', 'titanic')
#將輸入值整理為tuple 有參數可預先指定 args將抓取剩餘引數


#**來搜集關鍵字引數 函式內為字典
def book(**kwargs):
    print(kwargs)

book(name="jack",age=38,jpb='blacksmith')
#{'name': 'jack', 'age': 38, 'jpb': 'blacksmith'}


#the prime citizen of Python
def answer():
    print(42)

#括號代表呼叫此函式 不使用括號會被視為其他物件
answer()

#此函式功能為呼叫其他函式
def caller(others):#此others為python物件
    print("執行抓來的東西")
    others()#執行此物件


caller(answer)
#執行抓來的東西
#42

#引入函式其他範例
def adder(a,b):
    return a+b

def catcher(func,x,y):
    print(func(x,y))

catcher(adder,1,2)

#內部函式-可有效減少重複動作
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)

print(outer(9,8))#17

#lambda 匿名函式
def editer(words,func):
    for word in words:
        print(func(word))

def captitalizer(word):
    return word.capitalize()

cats=["meow","qq","ok"]

editer(cats,captitalizer)
#eow
#Qq
#Ok

#有效減少函式的數量與呼吸不順暢
editer(cats,lambda x:x.upper())
# MEOW
# QQ
# OK

#