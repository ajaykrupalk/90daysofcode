<h1>Recursion and Backtracking</h1>

<h3>Resources:</h3>
<li> Video for recursion: https://youtu.be/KEEKn7Me-ms
<li> Video for backtracking: https://youtu.be/DKCbsiDBN6c
<li> Theory for backtracking: https://www.programiz.com/dsa/backtracking-algorithm
  
<br>

<h3>Recursion:</h3>
Recursion is when a function calls itself. Every recursive function must have a base case or a stopping point.
<br><br>
Simplest example of recursive function is the <b>Fibonacci sequence:</b>
<br><br>

```python
def fib(n):
  if n<=0:#base-case
    return 0
  elif n==1:#base-case
    return 1
  else:
    return fib(n-1)+fib(n-2)
```

<br>
For example, if we wanted to find the fibonacci of 4:
<br><br>

fib(4) will break down to fib(3) and fib(2)
fib(3) will break down to fib(2) and fib(1)
fib(2) will break down to fib(1) and fib(0)
fib(1) will return 1
fib(0) will return 0
<br><br>

<h3>Backtracking:</h3>
<ul>
  <li>It is defined as a general algorithmic technique that considers searching every possible combination in order to solve a computational problem.
  <li>It uses Brute-force approach i.e. tries out all possible combinations and returns the best or desired solutions
</ul>
  
A <a href="https://cdn.programiz.com/sites/tutorial2program/files/ba-state-space-tree.png">space state tree<a/> is used to represent the solutions to a problem statement
<br>  
A standard backtracking problem is <b>N-Queen Problem</b>. It is the problem of placing N chess queens on a N*N chessboard so that no two queens attack each other. 
The idea is to place queens one by one in different columns, starting from the leftmost one. When we place a queen in a column, we check for clashes with already placed
queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. If we do not find such a row due to clashes
then we backtrack and return false.
