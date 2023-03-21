from sympy import *
'''
linear function: f(x) = mx+b, which is a line. m is slope, and b is y intercept.

example:
f(x) = 3x+1
m = 3
b = 1

on a graph
rise is m =3/1, so 3 is the rise, and 1 is the run. 
so a point, (0,1) and then a point, (1,4)

a line has a constant rate of change. in this case it's 3, same as slope.
'''

'''
constant rate of change
f(b) - f(a)/ b-a
From x=a to x=b
same as slope = y2-y1/x2-x1

'''

'''
Quadratic Function
f(x) = ax**2+bx+c

doesn't have a constant average rate of change.

f(x) = 4x**2+5x-7

wana find the average rate of change? Find it for these 2 thingamobobs
a) from 0 to 3
b) from 0 to -1

so f(b) - f(a) / b-a

so for the first one, f(3) - f(0) / 3-0 = something / 3. plug in the 3 into the function. so 44.
Then plug the zero into the function. so -7.
so 44- (-7)/ 3, which is 51/3, or 17. 

so a) the average rate of change is 17.

'''

# x = symbols('x')

def quadratic_function(x):
    return 4*x**2+5*x-7

'''
so we need to solve f(-1) - f(0) / -1 - 0

so eventually -8 - -7/3 which = -1/3
'''
# print(quadratic_function(3))

'''
graphs for quadratic function is a parabola. "U" or "^"
if it opens up, so "U", theres a minimum, and the other way theres a maximum.
so a > 0 and a < 0 respectively. 

our goal is to find what the max or min is.

The max or the min is are the vertex (h,k)
h= -b / 2a, then plug THAT into the function to get k,
so f(-b / 2a), and that will be the y coordinate

example: f(x) 4*x**2+5-7

determine if the graph opens up or down?
Does it have a max or min?
What is the it?

a = 4. it bigger than 0, so the graph is opening up "U". so there will be a minimum. 

h = -b / 2a = (-5)/2*4 = -5/8
so (-5/8,k)
'''
print( nsimplify(quadratic_function(-5/8)))

'''
so -137/16.

so the min is (-5/8, -137/16)
'''

# Does this open up or down? does it have a max or min? What is it then?
def example_function_1(x):
    return -3*x**2 + 6 - 7

'''
?
-3 is less than zero, so it opens down. "^". so it has a maximum

h = -6 / 2*-3
'''
print('h = ', (-6)/(2 * -3))
'''
so h = 1
'''
# print(nsimplify(example_function_1(1)))
'''
k is -4.
so (1,-4) is the maximum.

Technically the max is -4, but occurs at 1.
'''

'''
application function

give the revenue generated when selling some item at the unit price p


'''
# this is quadtric function, because of the p squared
def revenue(p):
    return -7*p**2 + 21000 * p
'''
a = -7, so theres a maximum and opens down.

so lets find the vertex to find the max.
b = -21000 / 2*-7 = 15,000
so (15000,k)
so revenue(15000) = supposed to be 15,750,000
'''
print(revenue(15000))