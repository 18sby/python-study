'''
  输出 100 - 999 之间的水仙花数
  153 = 3**3 + 5**3 + 1**3
'''

for num in range(100, 1000):
  ge = num % 10
  shi = num // 10 % 10
  bai = num // 100
  if ge**3 + shi**3 + bai**3 == num:
    print(num)