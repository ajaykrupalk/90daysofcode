#Fibonacci Number
#A precise solution using ternary operators
def fiboOne(n):
    #checking if n>2 since n=0 returns 0 and n=1 returns 1
    return fiboOne(n-1)+fiboOne(n-2) if n > 2 else 1

#Fibonacci Number - long method 
def fiboRecursive(n):
    if n > 2:
        return fiboRecursive(n-1)+fiboRecursive(n-2)
    else:
        return 1

print(fiboOne(12))
print(fiboRecursive(5))