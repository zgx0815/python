#1.解一元二次方程
import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
root = pow(b , 2) - 4 * a * c
if root > 0:
    r1 = (-b + math.sqrt(root)) / (2 * a)
    r2 = (-b - math.sqrt(root)) / (2 *a)
    print(r1 ,r2)
elif root == 0:
    r1 = -b / 2 * a
    print(r1)
else:
    print('The equation has no real roots')




#2.学习加法
import random

num1 = random.randint(0 , 100)
num2 = random.randint(0 , 100)
print(num1 , num2)
sum_ = int(input('亲，请输入这两个整数的和：'))
if num1 + num2 == sum_:
    print('答案正确，你真棒！')
else:
    print('答案错误，再试一次吧！')




#3.找未来数据
def week(day,fut):
    days = ['Sunday','Monday','Tuesday','Wendnesday','Thursday','Friday','Saturday']      #创建一个列表
    a = days[day]
    b = days[(day + fut) % 7]
    print("Today is %s and the future day is %s"%(a,b) )

def Start():
    day = int(input("Enter today's day:"))
    fut = int(input("Enter the number of days elapsed since today:"))
    week(day,fut)
Start()




#4.对三个整数排序
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
d = [a,b,c]
d.sort()     #升序sort()
print(d)




#5.比较价钱
money1 = float(input("请输入第一种大米的价钱："))
weight1 = float(input("请输入第一种大米的重量："))
money2 = float(input("请输入第二种大米的价钱："))
weight2 = float(input("请输入第二种大米的重量："))
per1 = money1 / weight1
per2 = money2 / weight2
if per1 > per2:
    print('第二种包装价格更好')
elif per1 < per2:
    print('第一种包装价格更好')
else:
    print('两种大米价格相同')




#6.找出一个月中的天数
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
list1 = [1,3,5,7,8,10,12]
list2 = [4,6,9,11]
if month in list1:
    print('%d年%d月份有31天'%(year,month))
elif month in list2:
    print('%d年%d月份有30天'%(year,month))
else:
    if year % 400 == 0 and year % 4 ==0:
        print('%d年%d月份有29天'%(year,month))
    else:
        print('%d年%d月份有28天'%(year,month))




#7.头或尾
import numpy as np 
res = np.random.choice(['正面','反面'])
print(res)
guess = input("请输入'正面','反面':")
if res == guess:
    print('恭喜你，答对啦！')
else:
    print('很遗憾，答错了!')




#8.剪刀石头布
import random
computer = random.randint(1,3)
print(computer)
user = int(input("请输入[1.石头 2.剪刀 3.布]"))
if computer != user:
    if  computer == 1  and user == 2:
        print('你输了，再来一局')
    elif computer == 2 and user == 3:
        print('你输了，再来一局')
    elif computer == 3 and user == 1:
        print('你输了，再来一局')
    else:
        print('你赢了，太棒了')
else :
    print('平局，再来一局')




#9.一周的星期几
year = int(input('请输入年份(eg.2008):'))
month = int(input('请输入月份(1-12):'))
days = int(input('请输入月份的第几天(1-31):'))
week = ['Saturday','Sunday','Monday','Tuesday','Wendnesday','Thursday','Friday']
if month == 1:
    month = 13
    year = year - 1
if month ==2:
    month = 14
    year = year - 1
h = int(days+((26*(month+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
day = week[h]
print('Day of the week is %s'%day)





#10.选出一张牌
import numpy as np 
card = np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
color = np.random.choice(['梅花','红桃','方块','黑桃'])
print('The card you picked is the %s of %s'%(card,color))




#11.回文数
num = int(input('亲，请输入一个三位数：'))
a = num % 10 *100 + num // 10 % 10 *10 + num // 100
if num == a:
    print('%d是回文数'%num)
else:
    print('%d不是回文数'%num)

#或者
num = input('输入一个三位数：')
a = num[2]
b = num[0]
if a == b :
    print('%r是回文数'%num)
else:
    print('%r不是回文数'%num)




#12.计算三角形的周长
a = int(input("请输入三角形的边长:"))
b = int(input("请输入三角形的边长:"))
c = int(input("请输入三角形的边长:"))
if a < b + c and b < a + c and c < b + a:
    sum = a + b + c
    print("三角形的周长是：%d"%sum)
else:
    print('亲，您输入的边长是不合法的哦！')




#13.统计正数和负数的个数然后计算这些数的平均值
positive_number = 0
negative_number = 0
sum_number = 0
for i in range(100):
    n = int(input('请输入整数:'))
    if n != 0:
        if n > 0:
            positive_number += 1
        else:
            negative_number += 1
    else:
        break
    sum_number += n
average_number = sum_number / (positive_number + negative_number)
print('您输入的正数有%d个，负数有%d个，平均值是%.2f'%(positive_number,negative_number,average_number))




#14.计算未来学费
money = 10000
ten_money = 0
for i in range(13):
    money = money * (1 + 0.05)
    if i == 9:
        print("十年后的学费是:%d"%money)
    if i >= 9:
        ten_money += money
print("十年后大学四年的总学费:%d"%ten_money)




#15.找出可以被5和6同时整除的数
count = 0
for i in range(100,700):
    if i % 5 == 0 and i % 6 == 0:
        print(i,end = " ")
        count += 1
        if count % 10 == 0:
            print()




#16.找出最小的n满足n²>12000；找出最大的n满足n³<12000；
n = 1
while n ** 2 < 12000:
    n += 1
print(n)

n = 1
while n ** 3 < 12000:
    n += 1
print(n-1)




#17.演示消除错误（1+1/2+1/3+.....+1/n）
a = 0
for i in range(1,5001):
    a += 1 / i
print('从左到右的和为：%r'%a)

b = 0
for i in range(5000,0,-1):
    b += 1 / i
print('从右到左的和为：%r'%b)




#18.数列求和(1/3+3/5+5/7+9/11+11/13+....95/97+97/99)

sum = 0
for i in range(1,99,2):
    j = i + 2
    sum += i / j
print("数列的和是:%f"%sum)




#19.计算∏=4（1-1/3+1/5-1/7+1/9-1/11+.....+(-1)**(i+1)/(2i-1)）

pai = 0
for i in range(1,100000):
    pai += 4 * ((-1) ** (i + 1) / (2 * i - 1))
print('pi = %r '%pai)




#20.完全数
for i in range(1,10000):     #i是在1~10000里的数
    a = 0    #除了本身的和
    for j in range(1,i):
        if i % j == 0:    #j是i的本身
            a += j
    if a == i:
        print(a,end = (" "))




#21.组合(7*6/2=21,)
count = 0
for i in range(1,8,2):
    for j in range(2,8):
        if i != j :
            count += 1
            print(i,j,end = "\n")
print("组合共有%d个数"%count)





