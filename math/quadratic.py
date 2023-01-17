from sympy import *

'''
quadratic day
variable has exponent

x2+5x+6=0 # 3 terms. use factor when theres no number in front of the x

4x**2 = 25 # use square root method

2x**2 - 7x+6 = 0 # 3 terms. use quadratic formula
'''

'''
x2+5x+6=0 # 3 terms, make sure they equal 0.
x**2 so 2 factors ()()
(x + 2)(x + 3) = 0
look at 6. what 2 numbers multiplied give 6, and add for 5. 2 * 3 = 6. 2 + 3 = 5.
x = -2 x = -3
'''
'''
x**2-5x+6 = 0
x = 2, x = 3
'''
'''
    2*x**2-7*x+6,0
 quadratic formula   x = -b+sqrt(b**2-4ac) / 2a
 x = (-7) +- sqrt( (-7)**2 - 4 (2)(6) ) / 2(2)
 x = 3/2, 2
'''

'''
4x**2 = 25
does not have 3 terms
options:
1. can you factor?
2. can you sqrt method
3. quadratic
we gonna use 2

Sqrt(4x**2) = +- sqrt(25)
'''
'''
(x+4)**2 = 13
'''
'''
overall strat
1) does it have 3 terms? 
    make sure it's equal 0. 
    if no number before x**[] factor if possible.
    if there is something before x**2, then quadratic formula

2) if theres 2 terms
    1. try sqrt method.
    2. factoring.

example of not doing sqrt method
x**2+3x=0
both terms have the variable.
factor out x instead
x (x+3) = 0
x = 0, x = x+3 [-3]
x = 0, x = -3
'''
'''
x**2-16 = 0 
- 16 + 16 = 0, 0 + 16 = 16
sqrt(x**2) = +-sqrt(16)
x= +- 4
'''
'''
b**2-4ac - the discriminate.
1) when it's positive, you get 2 real solutions and they're unique 
2) when it's zero it'll give 1 repeated real solution
3) if it's negative no real solution. it's a complex number
'''
x = symbols('x')



equation1 = Eq(
    (x - 5)**2,16
)
equation2 = Eq(
    x**2+2*x,8
)
equation3 = Eq(
    49 * x**2 + 9, 42 * x
)
equation4 = Eq(
    x**2 - 16, 0
)
print('#1', solve(equation1))
print('#2', solve(equation2))
print('#3', solve(equation3))
print('#4', solve(equation4))