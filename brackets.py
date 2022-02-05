def generateParanthesis(s,n,o=0,c=0,pos=0):
    if c==n:
        for i in s:
            print(i,end="")
        print()
        return
    else:
        if o > c:
            s[pos] = ")"
            generateParanthesis(s,n,o,c+1,pos+1)
        if o < n:
            s[pos] = "("
            generateParanthesis(s,n,o+1,c,pos+1)

n = 3
s = [""]*2*n
generateParanthesis(s,n)