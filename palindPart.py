def partition(s,i,res=[],part=[]):
    if i>=len(s):
        res.append(part.copy())#appending the existing copy of the partition
        print(res)
    for j in range(i,len(s)):
        if isPalind(s,i,j):#checking for palindrome
            part.append(s[i:j+1])#appending to the part array
            partition(s,j+1,part)#recursively calling next letter
            part.pop()#clearing part array for the next partition

def isPalind(s,i,j):
    res = s[i:j+1]
    if res == res[::-1]:
        return True
    return False

partition("geeks",0)