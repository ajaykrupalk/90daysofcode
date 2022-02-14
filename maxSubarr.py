nums = [-2,1,-3,4,-1,2,1,-5,4]
s = maxS = 0
for n in nums:
  s+=n
  if s < 0:
    s = 0
  maxS = max(maxS,s)
print(maxS)