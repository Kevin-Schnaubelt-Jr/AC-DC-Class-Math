from sympy import *
'''
list of them

1) Constant function f(x)=k, where k is a number.
on a graph it's just horizontal. y=k. Cross the y at k, so the y intercept is (0,k)

Properties of constant:
symmetrical to the y axis. which make sit EVEN. Constant on (-oo,oo). y intercept is (o,k)
domain: (-oo,oo)
range: k



2) Identity function - is a slanted line f(x)=x. Whatever input you give it matches the output.
Slanted line "/" because the input (x) is the same at output (y). so (1,1), (2,2), (3,3)
Domain: (-oo,oo)
Range: (-oo,oo)
symmetric to origins, so it's ODD.
y intercept is (0,0)
It's also increasing.



3) Square Function - f(x)=x**2 - So whatever the input is, the output will be input squared.
def function(x):
    return x**2

The graph is an upward parabola "U"
Domain: (-oo,oo)
Range: y >= 0 or [0,oo)
It's symmetrical to the y-axis, so it's EVEN.
It's also decreasing from (-oo,0) and increasing from (0,oo)



4) Cube Function f(x)=x**3 - You can have negative output functions unlike the squared one.
The graph looks like a origin symmetrical line 
"  |
"  /
"----
" /
"|

Domain: (-oo,oo)
Range: (-oo,oo)
Origin symmetry to ODD
y-intercepts (0,0)
It's increasing (-oo,oo)



5) Square Root Function f(x)=sqrt(x) - returns a FLOAT
Graph is a long going right from (0,0)
Domain: [0,oo]
Range: [0,oo]
y intercept is (0,0)
Not EVEN OR ODD
Increasing [0,oo]



6) Cube Root f(x) = cube root so cbrt(x).
Domain and range (-oo,oo)
ODD
y intercept is (0,0)
increasing on (-oo,oo)
print(cbrt(8))



7) Absolute Value - f(x) = |x| = {+x if x >= 0, -x if x < 0}
the graph is going to be a V from origin.
Domain: (-oo,oo)
Range: [0,oo) because y >= 0
EVEN because it has y axis symmetry
Decreasing from (-oo,0], and increasing from [0,oo)
Y intercept is (0,0)



8) Reciprocal Function - f(x) = 1/x - so, it inverts it for the output. Cannot put in 0!
Graph looks like it scales down. Never crosses the x or y-axis. The negative is mirrored.
zero will not be a value for x and y
so, Domain: All x, but x can't be zero. (-oo,0)U(0,oo) "U = union = OR"
Range: All y but y can't be zero. (-oo,0)U(0,oo)
ODD because of origin symmetry
Decreasing on the entire domain. (-oo,0)U(0,oo)
No y intercept
'''

'''
Piecewise function
Technically the absolute value function is one of these because it has 2 pieces, {x if x >= 0, -x if x < 0} = two conditionals. 
If, else, essentially.


example of a piecewise f(x) = {2*x - 1 if x > 1, 4*x if x <= 1}
'''

def piecewise_function(x):
    if x > 1:
        return 2*x - 1
    else:
        return 4*x
# print('piecewise function for 0 =',piecewise_function(0))
# print('piecewise function for 1 =',piecewise_function(1))
# print('piecewise function for 3 =',piecewise_function(3))
# print('piecewise function for -1 =',piecewise_function(-1))


# f(x) = {x**2 if x < 0, 2 if x = 0, 2*x + 2 if x > 0}
def piecewise_example_1(x):
    if x < 0:
        return x**2
    elif x == 0:
        return 2
    elif x > 0:
        return x*2 + 2
# print('piecewise example_1 for -1 =', piecewise_example_1(-1))
# print('piecewise example_1 for 0 =', piecewise_example_1(0))
# print('piecewise example_1 for 1 =', piecewise_example_1(1))

'''
graphing piecewise functions
example 1:
f(x) = {x if x != 0, -2 if x = 0}
the first if is an identity function, which is an increasing line intersecting the origin. Returns itself.
because of the the second if statement, there's going to be a hole at (0,0) because x can't be zero considering the conditional.
The second condition is a point (0,-2). It's a lone point.
So a line with a hole in the middle and a floating point.
Domain: (-oo,oo). It wouldn't have zero if it weren't for the second conditional.
Range: all y except 0. (-oo,0)U(0,oo) (x < 0 or x > 0)
Intercepts at (0,-2)

Example_2: 
f(x) = {3*x if x != 0, 3 if x = 0}
This is kind of an identiyy function, but with multiplied y by 3, so the line will get STEEPER.
With the condition of x != 0, we take out (0,0) leaving a hole.
Put a point at (0,3)
Domain: (-oo,oo)
Range: (-oo,0)U(0,oo)
Intercept is (0,3)

Example_3:
f(x) = {x + 5 if -4 <= x < 1, 8 if x = 1, -x + 3 if x > 1}
y=Mx + b
so the first if is a line - y = x + 5, y intercept (0,5), slope is 1.
so, a line from [-4,1)
Then there's just a point for (1,8)
the last condition is a line from (1,oo) with a hole at (1,2)
'''
def piecewise_example_2(x):
    if x >= -4 or x < 1:
        return x + 5
    elif x == 1:
        return 8
    elif x > 1:
        return -x + 3

# Homework ----
def homework_function(x):
    if x >= -3 and x <= 5:
        return 3*x-1
    # elif x == 0:
    #     return 0
    elif x > 5 and x <= 6:
        return x**3 - 5
print(homework_function(
    6
))