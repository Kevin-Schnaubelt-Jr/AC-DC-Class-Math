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

# def example_linear_1(x):
#     return 3*x+1

# print( (example_linear_1(1) - example_linear_1(3)) / (1-3)  )
# This equals 3, so then 3 over 1 3/1 is rise and run.

def example_linear_2(x):
    return (1/2)*x-6
print( nsimplify( (example_linear_2(-6) - example_linear_2(1/2)) / (-6-(1/2)))  )



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

def test_quad_func(x):
    return -3*x**2 + 6*x
the_h = -6/(2*-3)
the_k = test_quad_func(the_h)
print(f'{the_h=} {the_k=}')

def revenue(p):
    return -6*p**2 + 18000*p
the_h = -18000/(2*-6)
the_k = revenue(the_h)
print(f'{the_h=} {the_k=}')


# print( nsimplify(quadratic_function(-5/8)))

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
# print('h = ', (-6)/(2 * -3))
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
# print(revenue(15000))

'''
exmaple: f(x) = -2(x-1)**2 + 6
'''

def example_2(x):
    return -2*(x-1)**2 + 6

# print(nsimplify((0)))


'''
3/2 is h
'''

# print(nsimplify(example_2(0)))

'''
k is 11/2

so maybe (2/3, 11/2)

its actually (1,6) for some reason?

it was just change tehs lop into a possative, and then just 6
'''

def cost(x):
    return x**2 - 120*x + 7500

# so a > 0, so it opens up. so it has a minimum
a = 1
b = -120
h = -b / 2*a
# now we can find k
k = cost(h)
# print(f'{h=} {k=}')
# so the minimum marginal cost is 80, and it occurs at 2000 units.

# lets find the vertex of a function that turns -2*(x - 1)**2 + 5
def example_3(x):
    return -2*(x-1)**2 + 8

# so a < 0, so it opens down. so it has a maximum
# so for the vertex, h = 1 and k = 8
# to find the y-intercept, we just plug in 0 into the function
print(example_3(0),'y-intercept')
# to find the x-intercept, we let y = 0, and solve for x

# for example 4, we have f(x) = -(x - 3)**2 + 3
# so lets find the y-intercept
def example_4(x):
    return -(x-3)**2 + 3
print(example_4(0),'y-intercept')

# so for example 5, we have f(x) = (x-1)**2 + 2
# so lets find the y-intercept
def example_5(x):
    return (x-1)**2 + 2
print(example_5(0),'example_5 y-intercept')
