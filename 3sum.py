nums = [-1,0,1,2,-1,-4]
res = []
nums.sort()
for i,a in enumerate(nums):
  if i>0 and nums == nums[i-1]:
    continue
  l,r = i+1, len(nums)-1
  while l<r:
    threeSum = nums[i]+nums[l]+nums[r]
    if threeSum == 0:
      if [a,nums[l],nums[r]] not in res:
        res.append([a,nums[l],nums[r]])
      l += 1
    elif threeSum <0:
      l += 1
    elif threeSum >0:
      r -=1
print(res)