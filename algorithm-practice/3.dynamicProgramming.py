# 求凑齐 120 元，所需要的最少的方法？可选的面值有 1元、2元、5元
import sys
max = sys.maxsize

target = 120
coins = [1, 2, 5]

dp = []
dp.append(0)
dp.append(1)

for money in range(2,121):
  dp.append(max)
  dpLen = len(dp)
  for coin in coins:
    if money - coin > 0:
      dp[dpLen-1] = min(dp[money - coin] + 1, dp[dpLen-1])

print(dp[-1])