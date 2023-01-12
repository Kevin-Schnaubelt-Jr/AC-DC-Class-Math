from sympy import *

# linear equations

'''
example
(x+3)/2 + (x+6)/9 = 1

denominator removal. common denominator between 2 an 9, which is 18.
can also do 18/1

18/2 = 9, 18/9 = 2

9(x+3) +2 (x+6) + 18
9x+27+2x =18
11x+39 = 18
- 39     -39
11x = -21
/11    /11
x = -21/11

example 2
x/ (x-9) + 7 = 9 / (x-9)
LCD is x-9
(x-9) * x / (x-9), (x-9) * 7
x+7x-63 = 9
8x-63 = 9
8x = 72
/8   /8 = 9
x = 9 Which is wrong

example 3
x/ (x-2) + 1 = 2 / (x-2)

example 4
4x / (x**2 -4) = 8 / (x**2 - 4) * -3 / (x+2)s

example5
(5 * x) / (X**2 -25) = 25/ (x**2 -25) * -4/ (x+5)

example 6
Shannon's question
40x + 8(1.5x) = 494

'''
x = symbols('x')

equation = Eq(40 * x + 8 * (1.5 * x) , 494)
print(solve(equation))