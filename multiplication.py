#Problem: finding multiplication of a number using addition
#Solution: Adding the multiplier the number of multiplicand times
#4 * 5 = 4+4+4+4+4 = 20
def nTimesk(n,k):
    #n>1 is the base case
    return k+nTimesk(n-1,k) if n>1 else k
    #works as follows
    #4+4 = 8
    #4+8 = 12
    #4+12 = 16
    #4+16 = 20

print(nTimesk(4,5))