def add(a, b):
  return a + b

# 只有在点击运行 calc2.py 的时候，calc2 作为主程序的时候执行，才会执行此条件分支
if __name__ == "__main__":
  print(add(10, 20))