<h1>Resources</h1>
<br>

<h3>Recursive Digit Sum</h3>
<li>Problem Statement: https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
<li>Logic:
    <li>Take input of a number and the number of times it has to be appended to e.g. 9875 6
    <li>Find the sum of digits until it is a number < 10 e.g. for superDigit(9875) sum of digits < 10 = 2
    <li>Now take 8 and multiply it by k(the number of times it has to be appended to) e.g. 2*6 = 12
    <li>Since 12 is >=10 find the sum of digits until it is a single digit which is = 3
    <li>return 3 as the super digit