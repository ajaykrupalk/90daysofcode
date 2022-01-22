#Problem Name: Recursive Digit Sum
#The super digit of a number will be calculated as:
# super_digit(9875)   	9+8+7+5 = 29 
# super_digit(29) 	    2 + 9 = 11
# super_digit(11)	    1 + 1 = 2
# super_digit(2)		= 2  
#Given n = 9875 and k = 4
#p = 9875987598759875
# superDigit(p) = superDigit(9875987598759875)
#               9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
#superDigit(p) = superDigit(116)
#              1+1+6 = 8
#superDigit(p) = superDigit(8)
#since 8 is a number which is one digit, super-digit is 8
def superDigit(n,k):
    a = sumofDigits(str(n))
    s = a * k
    while s >= 10:
        s = sumofDigits(str(s))
    return s

def sumofDigits(n):
  if len(n) == 1:
    return int(n)
  else:
    return sumofDigits(str(sum(int(i) for i in list(n))))    

if __name__ == "__main__":
  n, k = map(int, input().strip().split(' '))
  print(superDigit(n,k))