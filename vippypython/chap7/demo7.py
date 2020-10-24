# 字典生成式
# zip 打包函数
# upper 字母转大写

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 200]

d = { item.upper():price  for item, price in zip(items, prices) }
print(d)