s = "pwwkew"
charSet = set()
l = res = 0
for r in range(len(s)):
  while s[r] in charSet:
    charSet.remove(s[l])
    l+=1
  charSet.add(s[r])
  res = max(res,len(charSet))
print(res)