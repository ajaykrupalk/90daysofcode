def checkDuplicate():
  dict = {}
  nums = [1,2,7,4]
  for i in nums:
    if i in dict:
      return True
    dict[i] = 1
  return False