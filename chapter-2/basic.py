#bool
True,False
a=True

#int
12,9000
b=55

#float
0.4,3.1415962,1.0e8
c=0.3

#str
"hey"
d="bye"

#變數/variable 
number=14

#know the type
print(type(a)) #bool
print(type(b)) #int
print(type(c)) #float
print(type(d)) #str

#python保留字 避免使用於變數設置
#continue,assert,in,with,lambda,if,try...

#計算
8+9
5-4
4*3
10/5

#取整數
7//2 #3

#取餘數
7%3 #1

#乘幕
3**4 #3*3*3*3=81

#自由發揮
h=4
2+(3*h) #14

#類型轉換
int(True)#1
int(False)#0
int(97.1)#97
int("-55")#-55
int("+4")#4
#無法處理含有小數點的字串
#int("97.1")#error

float(97)#97.0
float('97.1')#97.1

str(98.6)#"98.6"
str(True)#"True"

"hi this is a string"

#三引號用於多行字串，且能避免一些尷尬的"or'衝突
'''maybe we 
'should' do "more" 
practice right?'''

#運用\n換行
"or we\nshould\nbe\nlike\nthis"

#組合字串
print("hi"+"robot")#hirobot
print("ha"*4)#hahahaha

#印出資料
ok="enough"
print(99,"practice is not",ok)#99 practice is not enough

#[]擷取字元
says="abcdefg"
print(says[2])#c
print(says[-1])#g
print(says[1:])#bcdefg
print(says[2:4])#cd 2開始 4之前

#len()抓長度
print(len(says))#7

#split()分割
talk="my name is Yang"
print(says.split("c"))#['ab', 'defg']
print(talk.split())#['my', 'name', 'is', 'Yang']

#join()結合
x=",".join(says)
print(x)#a,b,c,d,e,f,g

#頭文字大寫
new_talk=talk.capitalize()
print(new_talk)#My name is yang

#全單字頭大寫
next_talk=talk.title()
print(next_talk)#My Name Is Yang

#全大寫
up_talk=talk.upper()
print(up_talk)#MY NAME IS YANG

#小寫
up_talk=talk.lower()
print(up_talk)#my name is yang

#大小對調
up_talk=talk.swapcase()
print(up_talk)#MY NAME IS yANG



#檢驗開頭與結尾
print(talk.startswith("my"))#True
print(talk.endswith("ng"))#True

#找字串
print(talk.find("is"))#8 第一次出現
print(talk.rfind("nam"))#3 最後一次出現

#出現次數
print(talk.count("n"))#2

#是否只有字元與數字
print(talk.isalnum()) #False 有空白
print(says.isalnum()) #True

#替換 replace something with something
print(talk.replace("Yang","nobody"))#my name is nobody

