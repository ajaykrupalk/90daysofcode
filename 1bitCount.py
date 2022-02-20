n = 0o11111111111111111111111111111101
res = 0
while n:
  n = n&(n-1)
  res += 1
print(res)