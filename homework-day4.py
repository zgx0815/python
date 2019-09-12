#1.定级

# scores = []
# for i in range(4):
#     num = int(input("input a number please: "))
#     scores.append(num)
# print (scores)    
# i = 0
# best = 100
# for i in range (4):
#     if int(scores[i]) >= best - 10:
#         print('student', i, 'scores is' ,scores[i], 'and grade is A' )
#     elif int(scores[i]) >= best - 20:
#         print('student' ,i, 'scores is' ,scores[i], 'and grade is B' )
#     elif int(scores[i]) >= best - 30:
#         print('student' ,i, 'scores is' ,scores[i], 'and grade is C' )
#     elif int(scores[i]) >= best - 40:
#         print('student' ,i, 'scores is' ,scores[i], 'and grade is D' )
#     else:
#         print('student', i ,'scores is' ,scores[i], 'and grade is F' )
#     i +=1




# 2.逆序读取的数字
# import random
# list = [random.randint(0,100) for i in range(10)]
# # print(list)
# print(sorted(list))  
# print(sorted(list ,reverse=True))




#3.统计数字个数
# list = list(map(int ,input('enter integers between 1 and 100:').split(',')))
# def count(var):
# #设置用于存储字符和次数的字典
#     result = {}
# #遍历容器中的所有数据
#     for i in var:
# #判断当前是否存在于字典中
#         if i in result:
#             result[i] = result[i] + 1
#         else:
#             result[i] = 1
# #返回结果
#     return result
# r = count(list)
# print(r)



	
#4.分析成绩
# list = list(map(int ,input('enter integers between 1 and 100:').split(' ')))
# def average (list):                             #计算平均值，精确到小数点
#     return float(sum(list))/len(list)
# num1 = 0
# num2 = 0
# def scord(list):
#     junfen = average(list)
#     for i in range(len(list)):
#         if list[i] >= junfen:
#             num1 += 1
#         else:
#             num2 += 1
#     print(junfen)
#     print(num1,num2)       




#5.统计单个数字
# import random
# # 随机数产生1000个整数(0-9),放入一个列表中,统计出现次数
# # 1.存放随机数列表
# number = []
# # 2.循环1000次
# for i in range(0,1000):
#     # 3.生成随机数
#     num = random.randint(0,9)
#     # 4.添加到列表中
#     number.append(num)
# print(number)
# # 5.统计每一个数字出现的次数
# result = {}
# # 把数字作为key,出现的次数作为值
# # 循环遍历每一个数字
# for num in number:
#     # 判断字典中是否有num这个key
#     if num in result.keys():
#         # 让数字对应的次数+1
#         result[num] += 1
#     else:
#         # 以数字作为key,值为1次
#         result[num] = 1
# # print(result.items())
# for i,num in result.items():
#     print("出现",i,"的次数为：",num,"次")




#6.找出最小元素的下标
# def indexOfSmallestElement(lst):
#     min = lst[0]
#     for i in lst:
#         if i < min:
#             min = i
#             return lst.index(min)
# a = [12,33,55,98,2,87,23,34,38,21]
# print(indexOfSmallestElement(a))




#7.随机数字选择器
# import random
# list = [20, 16, 12, 5]
# random.shuffle(list)
# print('随机排序列表：', list)
 



#8.消除重复
# def eliminateDuplicates(li): 
#     if len(li)!=len(set(li)):
#         print('亲，有重复哦') 
#     else:
#         print ('没有重复')
 
# if __name__ == '__main__':
#     li=[[1,2,3,4],[6,7,8],[4,5,6,6,6]]
#     for one_list in li:
#         print('one_list', one_list) 
#         eliminateDuplicates(one_list)




#9.判断有序吗？
# lst = list(map(int ,input('enter list:').split(',')))
# def isSorted(lst):

#     if lst == sorted(lst):
#         print('true')
#     else:
#         print('false')
# isSorted(lst)




#10.冒泡排序
# array = list(map(int ,input('enter ten number:').split(' ')))
# def main():
#     for i in range(len(array)):
#         for j in range(i):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     print(array) 
# if __name__ == '__main__':
#     main()


12.模式识别：四个连续的相同的数
