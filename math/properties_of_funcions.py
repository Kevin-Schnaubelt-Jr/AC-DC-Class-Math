from sympy import *

'''
topics
1) vertical line test
2) figuring out domain and range and intercepts from a graph
3) even and odd functions from graphing.
4) increasing, decreasing, and constant
5) finding max and min
'''

'''
vertical "VERTICAL" line test. see if graph is a function

VERTICAL line that intersects once is a function. 
more than once, not a function
'''

'''
domain, range, intercepts from graph
domain is all the points in between and including that farthest x-axis points.
the range is all the points in between and including the farthest y-axis points
just the points with 0 for x or y.

with arrows, things are different. since arrows pointing down south west and south east, all x values are -oo to oo.
so domain is (-oo,oo)
for the range, since the arrows are only pointing down, it's (-oo, highest y point]
'''

'''
Is the graph a function? What the domain and range? Intercepts? Symmetry.

2nd graph: ^
domain - [-pi,pi]
range - [-1,1]
intercepts - (-pi/2,0),(pi/2,0),(0,1)
is y-symmetrical

3rd graph: \_/
D: (-oo,oo)
R: [4,oo)
intercepts: (0,4)

4th graph: ^
D: (-oo,oo)
R: (-oo,4]
intercepts: (-6,0), (-2,0), (0,-5)
no symmetry
'''

'''
Even(2) and odd(1) functions - A function is even(2) if f(-x) returns f(x) and odd(1) if f(-x) returns -f(x).
or, even(2) if it has y axis symmetry, and odd(1) of it has origin symmetry.

'''
x = symbols('x')

def even_func(x):
    return simplify(9/(x**4))
# When this returns the function back unchanged, it's even(2).
# print(even_func(-x))

def second_func(x):
    return simplify(x**3-x)
# Not original, so not even. 
# print(second_func(-x))
# Lets see if its odd. A quick way to tell is if all terms are opposite signs. It is so we already know.
# But lets make sure by multiplying the function by -1.
# print(second_func(x) * -1)

# Here's some examples.

def is_it_even_or_odd(func, result):
    if func == result:
        return 'even'
    elif func * -1 == result:
        return 'odd'
    else:
        return 'neither'


def example_1(x):
    return simplify(3*x**2 + x - 1)
print('example 1', example_1(-x))
print('example 1 is', is_it_even_or_odd(example_1(x),example_1(-x)))

def example_2(x):
    return simplify(3/(x**10) - x**4)
print('example 2', example_2(-x))
print('example 2 is', is_it_even_or_odd(example_2(x),example_2(-x)))


def example_3(x):
    return simplify(7*x**3 + 3)
print('example 3', example_3(-x))
print('example 3 is', is_it_even_or_odd(example_3(x),example_3(-x)))


def example_4(x):
    return simplify((-7*x**3)/(3*x**2+8))
print('example 4', example_4(-x))
print('example 4 is', is_it_even_or_odd(example_4(x),example_4(-x)))

'''
Increasing and decreasing - from left to right, y coordinates is less on the second function so its increasing. 
y coordinates being less are decreasing
f(second x,y), f(first x,y) is increasing
f(first x,y), f(second x,y) is decreasing
constant is a horizontal line. So same y.

example: is f(x) decreasing on [-2,5]?
If it is decreasing, it needs to go down from [-2,5]
so on point f(x,-2) is lower, so its decreasing.

Constant is no change?

'''

'''
Local Max/ Min - (c, f(c))
Local max accurse x=c, local min accurse at x=c
So, for max, its at the apex of a curve decreasing to it's left and right, and for min, it's increasing to it's left and right.
'''

'''
example 1:
Question 1, is the graph increasing from -oo to -6 (-oo,6]?

Question 2, list the intervals of increasing and decreasing.

Question 3, identify and local max.

Question 4, identify and local min.


Answer 1: 
yes.

Answer 2: 
homework is looking for stuff le [-6,1], [3,6]

Answer 3:
homework will say "local max occur at "x= -6,3 and y= 12,4
It's just the maxs and mins x and y coordinates. 
'''

