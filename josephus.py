#The recursive function (josephus(n-1,k)+k-1)%n+1 explains as follows
#n-1 since there is going to be only one element remaining in the end
#+k-1 since we have to skip or move around the circle k-1 times
#%n since we are moving around a circle
def josephus(n,k):
    if n == 1:
        return 1
    return (josephus(n-1,k)+k-1)%n+1#perform this function with the different n values

print(josephus(11,2))