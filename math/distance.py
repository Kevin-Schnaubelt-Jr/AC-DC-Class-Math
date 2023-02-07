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


'''

equation = Eq(
    x, 0 + 5
)

print(
    solve(
        equation
    )
)
print('yo', sqrt(90)) ????
'''

'''
intercepts

(2,0) is an x intercept. always has a 0 for y
(0,3) is a y intercept. always has a 0 for x

5 * x + 4 * y = 20
'''

'''
equation_x = Eq(
    5 * x + 4 * 0, 20
)
equation_y = Eq(
    5 * 0 + 4 * x, 20
)

print(
    'x is (',
    solve(
        equation_x
    ),', 0)'
    ' y is (0,',
    solve(
        equation_y
    ),
    ')'
)
'''

'''
Ax+By=C is a line
y=Mx+b is a line

x and y dont have any exponents besides 1

example 
3 * x + 4 * y = 12
(4,0), (0,3)

y = 3 * x - 6
(2,0), (0, -6)
'''

'''
equation_x = Eq(
    4 * x**2 + 16 * 0**2, 64
)
equation_y = Eq(
    4 * 0**2 + 16 * x**2, 64
)

print(
    'x is (',
    solve(
        equation_x
    ),', 0)'
    ' y is (0,',
    solve(
        equation_y
    ),
    ')'
)
'''

'''
if y**2 that variable has 2 points. (0,y) and (0,y)

with 2 its nuts

4 * x**2 + 16 * y**2, 64
(-4,0) & (4,0), (0,-2) & (0,2)
'''

'''
symmetry

y - axis
x - axis

3 types

x axis symmetry
(3,4) => (3,-4)
y changes signs

y axis symmetry
(3,4) => (-3,4)
x changes signs

origin symmetry
(3,4) => (-3,-4)
original points flips over. x and y change signs
'''

'''
example
original point is (-3,2)
fin the new point after:
A) x - axis symmetry
B) y axis symmetry
C) original

A) (-3,-2)
B) (3,2)
C) (3,-2)
'''

'''
Graphs and Symmetry
y- axis symmetry | U or ^
(-3,9)      (3,9)
    (-2,5) (2,5)
        (0,1)

x - axis symmetry | < or >
        (4,4)
    (1,1)
(0,0)
    (1,4)
        (4,-4)

origin symmetry | / or \
                (2,8)
            (1,1)
        (0,0)
    (-1,-1)
(-2,-8)
'''

'''
determine intercepts and and symmetry
    >
(-5,0)
one intercept on the line. y is 0

    ^U
    (-5,5)
(-6,0),(0,0),(6,0)
          (5,-5)
3 intercepts on the line. ys are 0. and has origin symmetry as x and y change signs for that 5s points.


intercepts in symmetry
        |
--------[==]------
      //
     //
x intercepts are all values between 2 and 0 including 2, which is an interval. [2,0] is all our intercepts.
y intercept is (0,0)
'''