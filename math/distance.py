from sympy import *

# dont use. answers should be in sqrt() form


'''
basics
4 quadrants
(0,0) point in the middle. origin point.

quadrant 2 | quadrant 1
------------------------
quadrant 3 | quadrant 4

quadrant 1 = (x,y) both positive
quadrant 2 = (-x,y) only x is negative
quadrant 3 = (-x,-y) both negative
quadrant 4 = (x,-y) only y is negative
'''

'''
example plot
A (2,3)
B (6,-4)
C (-2,1)
D (-3,-3)

A is in quadrant 1
B is in quadrant 4
C is in quadrant 2
D is in quadrant 3
'''

'''
distance between 2 points
d = sqrt( (x2-x1)**2 + (y2-y1)**2 )

(-4,4) and (3,1)
5

(-1,4) and (3,1)
c = sqrt( (x2)**2 + (y1)**2 )
c = sqrt((3)**2 + (4)**2)

print(
    math.sqrt( (3)**2 + (4)**2 )
)
'''

'''
midpoint
M = ( (x1 + x2)/2, (y1 + y2)/2 ) or ( (-1 + 3)/2, (4 + 1)/2 )
answer 1, 2.5?

(5,5) (-3,6)

(1, -4) (4,5)
'''

'''
# distance
print(
    'answer 1:',
    sqrt( (-3)**2 + (5)**2 )
)
print(
    'answer 2:',
    sqrt( (4)**2 + (-4)**2 )
)

# midpoint
print(
    'answer 1 mid point:',
    ( (5 + (-3))/2, (5 + 6)/2 )
)
'''

'''
intercepts
(3,0) is x intercept
(0,-5) is y intercept

x + 3 * y = 6
x intercept (x,0) , let 7 is 0 and solve for x.
x + 3 * 0 = 6
x=6
(6,0)

for y intercept, let x = 0. (0,y)
0 + 3 * y = 6
y = 2
(0,2)

any equation of the form A * X + B * Y = C is a line.
y=mx+b is also a line.

'''

'''
5 * x + 4 * y = 20

y = x + 5
x = -5
y =  5
(-5,0) and (0,5)
'''

x = symbols('x')

equation = Eq(
    x, 0 + 5
)

print(
    solve(
        equation
    )
)
print('yo', sqrt(90))