# 密码如果错误,只能尝试3次机会.
# 验证码要有数字和字母滴组合. 区分大小写
# 验证码只能错5次.

# import random
# OPRIGINAL_USERNAME = 'admin'
# OPRIGINAL_PASScode = '111qqq...'
# COUNT = 1

# def check(username , passcode):
#     global OPRIGINAL_USERNAME , OPRIGINAL_PASScode , COUNT   
#     if username == OPRIGINAL_USERNAME and passcode == OPRIGINAL_PASScode:
#         print('登陆成功✌')
#     else:
#         print('账号或密码错误，登录失败😭')
#         if COUNT !=3:
#             COUNT += 1
#             login()
#         else:
#             print('尝试登陆次数达到上限,请去客服咨询,客服电话:13838384381')


# def login(): 
#     username = input('🙂，请输入账号>>')
#     passcode = input('🙂，请输入密码>>')
#     V_res = verify()
#     if V_res == True:
#         check(username ,passcode)
#     else:
#         for _ in range(4):
#             V_res = verify()
#             if V_res:
#                 check(username ,passcode)
#                 break
#         else:
#             print('验证码错误次数过多，请重新运行再次尝试👋！')
    
                
                
# def verify():
#     code = ''                                # 拼接随机生成的数字或字母
#     for _ in range(0, 4):                    #验证码设为四个循环4次生成4个字母或数字
#         nummber = str(random.randint(0, 9))      # 生成数字
#         character = chr(random.randint(65, 90))     # 生成字母  ASC码A:65~z:90
#         list = [nummber, character]                 #选出随机数和随机字母
#         choice_ = random.choice(list)
#         code = ''.join([code, choice_])  # 把code和ret用空字符串拼接;第一次一个空字符串+'a',code='a'
#     user_code = input('请输入验证码%s>>'%code)
#     if user_code == code:
#         return True
#     else:
#         return False    
# # verify()                  
# # login()  

# def start():
#     login()

# if __name__ == "__main__":
#     start()





#1.五角数
# def getPentagonalNumber(n):
#     count = 0
#     for i in range(1,n+1):
#         num = i * (3 * i -1) / 2
#         print('%r'%num,end = " ")
#         count += 1
#         if count % 10 == 0:
#             print('\n')

# getPentagonalNumber(100)




# 2.求一个整数各个数字的和
# def sunDigits(n):
#     sum_ = 0
#     m=len(str(n))
#     for i in range(m):
#         num = n // 10 ** i % 10
#         sum_ += num
#     print(sum_)

# if __name__ == "__main__":
#     n = int(input('请输入一个整数：'))
#     sunDigits(n)




# 3.对三个数排序
# def  displaySortedNumbers(num1 , num2 , num3 ):
#     a = [num1 , num2 , num3]
#     b = sorted(a)
#     print('按升序显示这三个数为：{}'.format(b))

# if __name__ == "__main__": 
#     num1 = int(input("请输入第一个数："))
#     num2 = int(input("请输入第二个数："))
#     num3 = int(input("请输入第三个数："))
#     displaySortedNumbers(num1 , num2 , num3 )




# 4.计算未来投资值(thinking)
# def futureInvestmentValue(investmentAmount , monthlyInterestRate , years):
#     for i in range(1 ,years + 1):
#         sum = investmentAmount * monthlyInterestRate * 0.01  
#         investmentAmount += sum
#         print(' %d 投资额：%.2f' % (i,investmentAmount))


# if __name__ == "__main__":
#     investmentAmount = float(input('请输入投资额：'))
#     monthlyInterestRate = float(input('请输入年利率：')) / 12
#     print('未来投资值为')
#     futureInvestmentValue(investmentAmount , monthlyInterestRate , years = 30)




# 5.显示字符(thinking)
# def printChars(ch1 , ch2 , numberPerLine):
#     for i in range(ch1 , ch2 + 1):
#         print(chr(i),end = " ")
#         if (i+2) % 10 == 0:
#             print()

# if __name__ == "__main__":
#     ch1 = 49
#     ch2 = 90
#     numberPerLine = 1
#     printChars(ch1 , ch2 , numberPerLine)




# 6.一年的天数
# def numberDaysInAYear(year):
#     for i in range(year , year + 11):
#         if i % 4 == 0 and i % 400 ==0 or i % 100 != 0:
#             print('{}年有366天'.format(i))
#         else:
#             print('{}年有365天'.format(i))

# numberDaysInAYear(2010)




# 7.几何问题：显示角(设A(X1,Y1)、B(X2,Y2)，则∣AB∣=√[(X1－X2)^2+(Y1－Y2)^2]=√(1+k^2)（∣X1－X2∣）^2)
def distance(x1 , y1 , x2 , y2):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    print('两点间的距离为：%.2f' %distance)
distance(2,3,4,1)

# 8.梅森素数




# 9.当前时间和日期




# 10.掷骰子
