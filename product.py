def productExceptSelf(arr):
  res = [1]*len(arr)

  prevProd = 1
  for i in range(len(arr)):
    res[i] = prevProd
    prevProd *= arr[i]
  
  nextProd = 1
  for i in range(len(arr)-1,-1,-1):
    res[i] *= nextProd
    nextProd *= arr[i]
  
  return res

print(productExceptSelf([1,2,3,4]))