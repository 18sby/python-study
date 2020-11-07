# 多个数字随机组合的所有方式

origin = [1,2,3]
olen = len(origin)
lst = []

def dfs(current, store, l):
  if len(current) == l:
    lst.append(current.copy())
    current = []
    return
  for index, item in enumerate(store):
    next = current.copy()
    next.append(item)
    dfs(next, store[0:index:1] + store[index+1::1], l)

dfs([], origin, olen)

print(lst, len(lst)) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 6