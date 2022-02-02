def findSumOf(a, b, c,n):
  if n == 1:
    return a
  if n == 2:
    return b
  if n == 3:
    return c
#returns the sum of the last three numbers
  return findSumOf(a,b,c,n-1)+findSumOf(a,b,c,n-2)+findSumOf(a,b,c,n-3)

t = int(input())
arr = []
for i in range(t):
  a,b,c,n = input().split()
  a,b,c,n = list(map(int,(a,b,c,n)))#mapping the input to integers
  arr.append(findSumOf(a,b,c,n))
#prints the results of each input one after the other
for i in arr:
  print(i)