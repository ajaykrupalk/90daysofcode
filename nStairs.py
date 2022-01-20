#Problem: Davis has a number of staircases in his house and he likes to climb each staircase 1,2, or 3 steps
#at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
#Naive-Solution: Using recursion, the time complexity is O(3^n)

def findSteps(n):
    if n==0:#if bottom-most step is reached
        return 1
    elif n<0:#if a negative number is reached
        return 0
    else:
        return findSteps(n-3)+findSteps(n-2)+findSteps(n-1)

print(f"No. of ways to climb 4 steps: {findSteps(4)}")