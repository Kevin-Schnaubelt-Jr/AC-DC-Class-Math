from sympy import *

x = symbols('x')

'''
1) composite functions
2) one-to-one function
3) inverse function
'''

'''
composite function
(fog)(x)=f(g(x))
open dot in "fog" means take the composition of f after you apply g.

its just a nested function.
'''

def composite_function_example_f(x):
    return 2 * x

def composite_function_example_g(g):
    return g-1

# so FoG
# print(composite_function_example_f(composite_function_example_g(0)))
# -2

# now GoF
# print(composite_function_example_g(composite_function_example_f(1)))
# 1

# now GoG
# print(composite_function_example_g(composite_function_example_g(2)))
# 0

def function_f_1(x):
    return 3*x

def function_g_1(x):
    return 6*x**2+6

# a) (fog)(4)
# print(function_f_1(function_g_1(4)))
# 306

# b) (gof)(2)
# print(function_g_1(function_f_1(2)))
# 222

# c) (fof)(1)
# print(function_f_1(function_f_1(1)))
# 9

'''
f(x) = 4*x+8
g(x) = x**2
to where putting just x**2 INTO f(x**2)
this is for fog

for gof, put in f(4*x+8)
'''

'''
horizontal test for a one to one. if it intersects twice its not one to one.
'''

'''
inverse function
notation f**-1(x) represents the inverses of f(x).
if f(x) is one-to-one, then the inverse is f**-1(x). really just switching x and y.
so, (2,4) becomes (4,2).
reflects across the y=x line. Domain and the range switch.

example:
heres some points: (1,2), (3,4), (6,8), (-1,3), = f
Q1: What is the domain and range of f
Q2: If f one to one
Q3: If so, whats the inverse? f**-1?
Q4: Domain and range of the inverse f**-1.


A1: Domain 1,3,6,-1 | range is 2,4,8,3
Q2: all y coordinates are unique, so it is one to one.
f**-1 = (2,1), (4,3), (8,6), (3,-1)
'''

'''
relationship between composite functions and inverse functions. 
f and g are inverse if:
1) (f o g)(x) = x
2) (g o f)(x) = x

example
f(x) = -2*x + 3
g(x) = -1/2 * (x - 3)

lets check:
(f o g)(x) = f(g(x)) = f(-1/2*(x - 3)) = -2(-1/2*(x - 3))+ 3 = x

(g o f)(x) = g(f(x)) = g(-2*x + 3) = -1/2*(-2*x + 3 - 3) = x

so yes, they are inverses.
'''

'''
try this:
f(x) = -4*x + 4
g(x) = -1/4*(x - 4)
'''

def function_f(x):
    return nsimplify(simplify(-4*x + 4))

def function_g(x):
    return nsimplify(simplify(-1/4*(x - 4)))
    

print('f o g = ',function_f(function_g(x)))
print('g o f = ', function_g(function_f(x)))

'''
yep, both are x, so it's inverse.
'''

'''
one more example:
f(x) = x**3 - 6
g(x) = cbrt(x + 6)
'''

def function_f2(x):
    return x**3 - 6

def function_g2(x):
    return cbrt(x + 6)

# print('f o g = ',function_f2(function_g2(2)))
# print('g o f = ', function_g2(function_f2(2)))

# this function with verify that the function is one to one.

def one_to_one(f, a, b):
    '''
    f: function
    a: lower bound
    b: upper bound
    '''
    # create a list of all the values of f(x) for x in the range [a,b]
    # f_values = [f(x) for x in range(a,b)]
    f_values = []
    for x in range(a,b):
        f_values.append(f(x))
    # check if the list has any duplicates
    if len(f_values) == len(set(f_values)):
        return True
    else:
        return False
    
# this function will verify that a function is the inverse of another function.
def inverse(f, g, a, b):
    '''
    f: function
    g: function
    a: lower bound
    b: upper bound
    '''
    # create a list of all the values of f(g(x)) for x in the range [a,b]
    # f_values = [f(g(x)) for x in range(a,b)]
    f_o_g_values = []
    g_o_f_values = []
    for x in range(a,b):
        f_o_g_values.append(f(g(x)))
    for x in range(a,b):
        g_o_f_values.append(g(f(x)))

    for index, value in enumerate(f_o_g_values):
        if value != g_o_f_values[index]:
            return 'Not inverse'
    return 'Inverse'
    
# print(inverse(function_f, function_g, -10, 10))

# make another inverse function that takes in sympy symbol x as an argument instead of a range.

def inverse2(f, g, x):
    if f(g(x)) == x and g(f(x)) == x:
        return 'Inverse'
    else:
        return 'Not inverse'
    
print(inverse2(function_f, function_g, x))
