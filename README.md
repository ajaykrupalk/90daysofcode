<h1>Asymptotic Notation/Big O notation</h1>
<p>
    Big-O Notation represents the upper bound of the running time of an algorithm. Thus, it gives the worst-case complexity of an algorithm.
</p>
<h3>Steps to follow for Big-O Notation</h3>
<ol>
    <li>
        Different steps get added: <br>
        ```
            def something():
                doStep1()#O(a)
                doStep2()#O(b)
        ```
        <br> Time complexity of function is O(a+b)
    </li>
    <li>
        Drop constants: <br>
        ```
            def minMax1(array):
                min,max = NULL
                for e in array:#O(n)
                    min = MIN(e,min)
                for e in array:#O(n)
                    max = MAX(e,max)
        
            #Time complexity of above function is O(n)            
        
            def minMax2(array):
                min,max = NULL
                for e in array:#O(n)
                    min = MIN(e,min)
                for e in array:#O(n)
                    max = MAX(e,max)
        
           #Time complexity of above function is O(n)
        ```
        <br>Time complexity of program is O(2n) = O(n)
    </li>
    <li></li>
    <li></li>
</ol>
