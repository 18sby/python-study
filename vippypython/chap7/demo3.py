# 键的判断

score = { '张三': 100, '李四': 98, '王五': 99 }

print('张三' in score)
print('张三' not in score)

# del dict[key] 删除字典的键
del score['李四']

# dict.clear() 清空字典
score.clear()
print(score)

# 新增元素
score['陈柳'] = 99.5
print(score)

# 修改元素
score['陈柳'] = 101
print(score)