arr = [6, -3, -10, 0, 2]
res = 0
curMax = curMin = 1
for n in arr:
  if n == 0:
    curMax = curMin = 1
    continue
  prevMax = curMax * n
  curMax = max(n*curMax,n*curMin)
  curMin = min(prevMax,n*curMin)
  res = max(res, curMax)
print(res)