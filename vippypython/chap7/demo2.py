# 获取字典中的值

score = { '张三': 100, '李四': 98, '王五': 99 }

# 1. dict[key]
print(score['张三'])
# print(score['陈柳']) # 报错 KeyError

# 2. dict.get(key)
print(score.get('李四'))
print(score.get('陈柳')) # None
print(score.get('马七', 99)) # 第二个参数是在查找指定 key 不存在的时候，设置的默认值