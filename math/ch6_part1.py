from sympy import *

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

