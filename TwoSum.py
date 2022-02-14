arr = [2,1,7,5,3]
target = 9
for i in range(0,len(arr)):
    if target- arr[i] in arr:
        print([i,arr.index(target- arr[i])])
        break
