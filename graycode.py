#counts the number of 1s in the binary representation of number
def countOnes(n,count=0):
  if n>=1:
    if n%2 == 1:
      count = count+1
    return countOnes(n//2,count)
  return count

#finding if two numbers differ by 1 bit using xor operation
def differBit(x,y):
  return countOnes(x^y)==1

#converting to binary
def toBinary(n):
  if n>=1:
    toBinary(n//2)
  print(n%2,end="")

nums = set()
for i in range(0,4):
  for j in range(i+1,4):
    if differBit(i,j):
      if i in nums:
        toBinary(j)
        print()
      elif j in nums:
        toBinary(i)
        print()
      else:
        toBinary(i)
        print()
        toBinary(j)
        print()
      nums.add(i)
      nums.add(j)
      break