#recursive function to find prime number
def isPrime(n, i=2):
    if n == 2 or n == 1:
        return True
    if i == n:
        return True
    if n % i == 0:
        return False
    return isPrime(n, i + 1)

#function to find if array is palindrome
def isPalindrome(arr):
  return arr == arr[::-1]

#finding distinct arrays
def multipleValue(arr,p,n,temp=[],i=0,j=2):
  if i==n:
    return temp
  if j<=n:
    if arr[i]**j < p and isPalindrome([arr[i]]*j):
        temp.append([arr[i]]*j)
    return multipleValue(arr,p,n,temp,i,j+1)
  if j>=n:
    return multipleValue(arr,p,n,temp,i+1,j=2)

#calling the actual functions
def solve(n,p):
  arr = []
  for i in range(2,p):
    if isPrime(i):
      arr.append(i)
  for i in arr:
    print([i])
  for i in multipleValue(arr,p,n):
    print(i)

solve(3,10)