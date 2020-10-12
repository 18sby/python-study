'''
  从键盘录入两个整数，比较大小
'''

numA = int(input('请输入第一个整数'))
numB = int(input('请输入第二个整数'))

# 正常写法
# if numA >= numB:
#   print(numA, '大于等于', numB)
# else:
#   print(numA, '小于等于', numB)

# 使用条件表达式简写上面代码
# 条件为True的输出 条件 条件为False的输出
print( (str(numA) + '大于等于' + str(numB)) if numA >= numB else (str(numA) + '小于等于' + str(numB)) )