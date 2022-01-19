from math import sqrt

#Best Solution: Recommended by Hackerrank
#Time complexity is O(sqrt(n))

def primality(n):
    #checking the base condition
    if n==2:
        return "Prime"
    #all numbers<1 and even numbers greater than 2 are not prime
    elif (n<=1 or (n & 1)==0):
        return "Not prime"
    #checking for prime numbers starting from 3
    #increementing by 2 as we are checking for all odd numbers
    for i in range(3,int(sqrt(n+1))+1,2):
        if n%i ==0:
            return "Not prime"
    return "Prime"

print(primality(3)) 
