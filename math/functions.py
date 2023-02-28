from sympy import *
from sympy.utilities.lambdify import implemented_function

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
    function_negativity = 1
    if x == '-x':
        x = (-symbols('x'))
    elif x == 'negative x':
        x = symbols('x')
        function_negativity = -1
    elif x == 'test':
        x = (symbols('x') + 3)
        return nsimplify(3 * x**2 + 2 * x - 4)
    else:
        x = int(x)
    return nsimplify(3 * x**2 + 2 * x - 4) * function_negativity

# print(
#     function_1(input('>: '))
# )
x = symbols('x')
h = symbols('h')
f = implemented_function('f', lambda x: 3 * x**2 + 3 * x - 2)
lam_f = lambdify(x, f(x))
print(lam_f(x) * -1)

'''
find the domain

example 1: x as a fraction
f(x) = (2*x) / (x**2-25)

example 2:
y = 3*x**2+4*x-2

example 3:
g(x) = sqrt(-2*x-4)
'''

'''
example 1:
dominator is x**2-25 = 0
so add 25 to both sides, then sqrt both sides
so x**2 = 25
x = +- 5

so domain is all x but ! -5,5
(-oo,-5)U(-5,5)U(5,oo)
'''
'''
example 2:
(-oo,oo) because no fractions or sqrt
'''
'''
example 3:
so set -2*x-4 >= 0
so add 4.
-2*x>=4
so divide -2 divide or multiply by a negative flop the inequality
x >= -2
(-oo,-2]
'''

'''
example 4: find domain
p(t) = (sqrt(t-6)) / (3*t-24)

case 1 denominator 3*t-24=0
add 24
3*t=24
divide 3
t = 8
so 8 is excluded by the domain.

case 2 squart root
set t - 6 >= 0
add 6
t >= 6
so domain is everything great than or equal to 6, but not 8
[6,8)U(8,oo)
'''

'''
if -f(x)
multiple equation by -1

'''