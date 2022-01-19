<h1>Asymptotic Notation/Big O notation</h1>
<p>
    Big-O Notation represents the upper bound of the running time of an algorithm. Thus, it gives the worst-case complexity of an algorithm.
</p>
<h3>Steps to follow for Big-O Notation</h3>
 1. Different steps get added

```python
def something():
    Step1()#O(a)
    Step1()#O(b)
    
#Time complexity of function is O(a+b)
```

2. Drop the constants

```python
def minMax1(array):
    min,max = NULL
    for e in array:#O(n)
        min = MIN(e,min)
    for e in array:#O(n)
        max = MAX(e,min)
        
#Time complexity of function is O(n)

def minMax2(array):
    min,max = NULL
    for e in array:#O(n)
        min = MIN(e,min)
        max = MAX(e,min)
        
#Time complexity of function is O(n)

#Time complexity of program is O(n+n) = O(2n) = O(n)
```

3. Different inputs = Different variables

```python
def intersectionSize(arrayA,arrayB):
    count = 0
    for a in arrayA:#O(a)
        for b in arrayB:#O(b)
            if a == b:
                count += 1
    return count
        
#Time complexity of function is O(a*b)

```

4. Drop non-doominant terms


```python
def something(array):
    max = NULL
    for a in array:#O(n)
        max = MAX(a,max)
    print(max)
     #Time complexity is O(n)
    
    for a in array:#O(n)
        for b in array:#O(n)
            print(a,b)
    #Time complexity is O(n^2)
    
#Time complexity of program is O(n+n^2) = O(n^2)

```
