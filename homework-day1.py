
#1.将摄氏温度C转换为华氏温度F
# fahrenheit= 1.8C + 32
# C = float(input('请输入摄氏温度: '))
# F = 1.8*C + 32
# print('%.1f摄氏度 = %.1f华氏度' % (C, F))




#2.计算圆柱体的体积
# import math
# radius=float(input('请输入圆柱体的半径：'))
# high=float(input('请输入圆柱体的高：'))
# area=radius *radius * math.pi
# volume = area * high
# print('圆柱体的底面积为：%.2f' %area)
# print('圆柱体的体积为：%.2f' %volume)




#3.将英尺数转换为米数
# Foot=float(input('请输入英尺数：'))
# meters=0.305 * Foot
# print ('%.4f英尺 = %.4f米' %(Foot , meters))




#4.计算能量
# M=float(input('请输入按千克计算的水量：'))
# inialtemperature=float(input('请输入水的初始温度：'))
# finaltemperture=float(input('请输入水的最终温度：'))
# Q=M * (finaltemperture - inialtemperature) * 4184
# print ('所需的能量为：%.2f' %Q)




#5.计算利息
# balance=float(input('请输入差额：'))
# annual_interest_rate =float(input('请输入年利率：'))
# Interest= balance* (annual_interest_rate /1200)
# print ('下个月所需要付的利息为：%f' %Interest)




#6.加速度
# v0=float(input('请输入初始速度：'))
# v1=float(input('请输入末速度：'))
# t=float(input('请输入速度变化所占用的时间：'))
# a=(v1 - v0) / t
# print ('平均加速的为：%.4f' %a)




#7.复利值
# save_amount=float(input('请输入每月存款数：'))
# rate=0.05/12
# interest = 1 + rate
# count=[0]
# for i in range(6):
#     sum = (100 + count[i]) * interest  
#     count.append(sum)
# print('六个月后的账户总额：%.2f' % count[6])




#8.对一个整数中的各位数字求和
# num=float(input('请输入一个0-1000之间的整数：'))
# bai=int(num // 100)
# shi=int(num //10 %10)
# ge=int(num %10 )
# sum =bai +shi +ge 
# print('各位数字之和为:%d' %sum)





#3.1一个五边形的面积
# import math
# r=float(input('请输入顶点到中心的距离：'))
# s=2*r*math.sin(math.pi/5)
# area=(5*s*s)/(4*math.tan(math.pi/5)) 
# print('五边形的面积为：%.2f' %area)





#3.2大圆距离
# import math
# x1,y1 = eval(input('请以度为单位输入点1(纬度和经度):'))
# x2,y2 = eval(input('请以度为单位输入点1(纬度和经度):'))
# radius = 6371.01
# x11 = math.radians(x1) #math.radians()函数将度数转换成弧度数
# y11 = math.radians(y1)
# x22 = math.radians(x2)
# y22 = math.radians(y2)
# d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
# print('两点之间的距离为： %.2f km'%d)




#3.4一个正多边形的面积
# import math
# n=int(input('请输入边的数目：'))
# side=float(input('请输入多边形的边长：'))
# area=(n*side*side)/(4*math.tan(math.pi/n)) 
# print('五边形的面积为：%.5f' %area)




#3.5找出ASCII码的字符
# num=int(input('请输入一个0~127之间的整数：'))
# char=chr(num)
# print('%d对应的字符为：%c'%(num,char) )
# character=input('请输入字符：')
# number=ord(character)
# print('%c对应的数值为：%d'%(character,number) )





#3.6工资表
# name=input('雇员姓名：')
# time=eval(input('一周工作时间：'))
# pay_rate=eval(input('每小时报酬：'))
# federal_rate=eval(input('联邦预扣税率：'))
# state_rate=eval(input('州预扣税率：'))
# Federal =time  * pay_rate * federal_rate
# State = time * pay_rate * state_rate
# Gross = time * pay_rate
# NetPay = time * pay_rate - Federal - State
# Total = Federal + State
# print('雇员姓名：' ,name）
# print('一周工作时间：' ,time)
# print('每小时报酬：' ,pay_rate)
# print('GrossPay:'Gross )
# print('Deductions:')
# print("\tFederal withholding (20.0%):KaTeX parse error: Expected 'EOF', got '\tState' at position 19: …ederal) print("\̲t̲S̲t̲a̲t̲e̲ ̲withholding (9.…",State)
# print("\tTotal Deduction:&quot;,Total)print(&quot;NetPay: &quot;,Total)print(&quot;Net Pay:",Total)print("NetPay:",NetPay





#3.7反向数字
# num = int(input("请输入一个四位数:"))
# i = 0
# num1 = num
# while True:
#     if num1 // 10 == 0:
#         break
#     i += 1
#     num1 = num1 // 10
# sum = 0
# while i >= 0:
#     sum = sum + (num % 10) * (10 ** i)
#     num = num // 10
#     i = i - 1
# print(sum)




# Number = input('number:>>')
# if len(Number) > 3:
#     print('[!] Error, The lenghts must be Three!!')
# else:
#     bai = int(Number[0])
#     shi = int(Number[1])
#     ge = int(Number[2])
#     if bai ** 3 + shi **3 + ge **3 == int(Number):
#         print('水仙花')
#     else:
#         print('不是')




# for i in range(10):
#     print('. ',end="")
# print()
# for k in range(8):
#     print('. ',' '*16,'. ',sep="")

# for j in range(10):
#     print('. ',end="")       



# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\或()折行
# is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(is_leap)



# a = 5
# b = 10
# c = 3
# d = 4
# e = 5
# a += b
# a -= c
# a *= d
# a /= e
# print("a = ", a)

# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print(flag1 is True)
# print(flag2 is not False)




# email = input('Input your email:')
# for j in email:
#     ord_ = ord(j)
#     ord_1 = ord_ + 10
#     str_ = chr(ord_1)
#     print(str_,end="")



# 小案例:计算器
# input_1 = input('请输入一个数字:>>')
# input_2 = input('请输入一个数字:>>')
# ChangeToFloat_1 = float(input_1)
# ChangeToFloat_2 = float(input_2)
# Calc_Add = ChangeToFloat_1 + ChangeToFloat_2
# print("答案是:",Calc_Add)




# 格式化输出:
# print('{} 真帅'.format('张琦妮'))
# """
# # 格式化输出
# 1. % 作为一个连接, %s,%d,%f: 保留小数位%.2f
#     print('%.2f + %.2f = %.2f'%(num1,num2,num1+num2))
# 2. format
#     print('{} + {} = {}'.format(num1,num2,num1+num2))
#     保留小数位:
#     print('{:.2f} + {:.2f} = {}'.format(num1,num2,num1+num2))




# print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))
# print('\n'.join([''.join([('AndyLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
# print('\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else' 'for x in range(-80,20)])for y in range(-20,20)]))




# import random
# import string
# p="".join([random.choice(string.ascii_letters) for i in range(5)])
# q="".join([random.choice(string.ascii_letters+string.hexdigits) for i in range(6)])
# print(p)
# print(q)
# p,q就是初始化的用户和密码,p是用户名,q是密码，可以打印，可以不打印 
# flag，count是计数器
# flag=0
# count=0
# while True:
#     username=input("输入你的名字:")
#     if username == p:
#         while True:
#             passwd=input("输入你的密码")
#             if passwd == q:
#                 print("成功进入")
#                 break
#             else:
#                 flag+=1
#                 print('密码错误')
#                 if flag == 3:
#                     print('密码错误三次')
#         break
#     else:
#         count+=1
#         print('用户名错误')
#     if count == 3:
#         print('用户名错误过多')
#         break




# 编写一个函数，接收传入的字符串，统计大写字母的个数、小写字母的个数、数字的个数、其它字符的个数，并以元组的方式返回这些数，然后调用该函数；
# import sys
# def deal_char(li):
#     list=[]
#     # list.append(float(max(li)))
#     # list.append(float(min(li)))
#     upper=0
#     lower=0
#     num=0
#     other=0
#     # str.__len__()
#     for i in  range(li.__len__()):
#         if li[i].isupper():
#             upper+=1
#         elif li[i].islower():
#             lower+=1
#         elif li[i].isnumeric():
#             num+=1
#         else:
#             other+=1
#     list.append(upper)
#     list.append(lower)
#     list.append(num)
#     list.append(other)
#     print("list:",list)
#     return tuple(list)
# if __name__=="__main__":
#     # print("请输入一个序列：")
#     # while
#     ll=input("please input some char(or a string):",)
#     # print(type(lll))
#     deal=deal_char(ll)
#     print("tuple contain count with upper char,lower char ,number and others:",deal)




# 九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            print("%d*%d=%d\t" % (j, i, i*j), end="")
        print()

#斐波那契数列  0，1，1，2，3，5，8,...
num=int(input("需要几项？"))
n1=0
n2=1
count=2
if num<=0:
    print("请输入一个整数。")
elif num==1:
    print("斐波那契数列:")
    print(n1)
elif num==2:
    print("斐波那契数列:")
    print(n1,",",n2)
else:
    print("斐波那契数列:")
    print(n1,",",n2,end=" , ")
    while count<num:
        sum=n1+n2
        print(sum,end=" , ")
        n1=n2
        n2=sum
        count+=1
print()
#阿姆斯特朗数
#如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
num = int(input("请输入一个数字: "))
sum = 0
n = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if num == sum:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")
