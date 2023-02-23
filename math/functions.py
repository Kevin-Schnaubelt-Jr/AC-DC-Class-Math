from sympy import *

'''
a "Function" is a rule or assignment that takes in an input (x) and maps it to some output (y)
(x) is  called an independent variable and (y) is called the dependant variable.

domain [x] f => co-domain [y] range: 
"domain" is span of the input and "range" is the span of the output.

function notation : f(x)
(x) is the input or argument.

example: 
f of x : f(x) = 2*x+1
2*x+1 is the function and y is the output
so, 
def function(x):
    y = 2*x+1
    return y
'''

'''
example of a set of points:
(-1,2), (3,4), (6,8), (7,2) = f
whats the domain? Does this represent a function?
domain is all the x values from left to right
D = -1,3,6,7

range is all the y's WITHOUT repeats.
R = 2, 4, 8

this is a function because each input (x) is unique.

example 2:
(-1,2), (4,6), (-1,7), (2,3)
D = -1, 4, -1, 2
R = 2, 6, 7, 3

Not a function because it has repeated inputs (-1).

example 3:
f = (-1,0), (4,0), (6,0), (8,1)
I guess the (x) and (y) of the points are the inputs and outputs.
This is a function because no inputs are repeated.

example 4:
f = (0,4), (-2,8), (8,-2), (0,6)
not a function obviously.
'''

'''
most of the time the function is given by an equation, which can be graphed.
With an equation, it means you usually have an infinite amount of points.
so f(x) = 2*x+1 is a line. so y = m*x+b
slope 2
y intercept (0,1)
because it goes from -oo to oo the domain is (-oo,oo)
'''

def function_1(x):
    if x != 'x' and x != '-x':
        x = int(x)
        return 3 * x**2 + 2 * x - 4
    else:
        x = symbols('x')
        return solve(3 * x**2 + 2 * x - 4)

print(
    function_1(input('>: '))
)