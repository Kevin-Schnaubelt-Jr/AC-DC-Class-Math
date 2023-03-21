from sympy import *
from sympy.utilities.lambdify import implemented_function


# Lines
def find_b(x,y,m):
    b = symbols('b')
    equation = Eq(
        y, m*x+b
    )
    b_equals = nsimplify( solve(equation)[0])
    print(
        'b = ',
        b_equals
    )
    return b_equals
    
# find_b(-2,-7,2)


def find_m(x_1st,y_1st,x_2nd,y_2nd):
    m = nsimplify( (y_2nd - y_1st) / (x_2nd - x_1st) )
    print('m = ', m)
    b = find_b(x_1st,y_1st,m)
    plus_or_minus = '+ '
    if b < 0:
        plus_or_minus = ''
    print(f'so, y = {m}x {plus_or_minus}{b}')
# find_m(3,-6,5,-5)

# fairly simple. Just the formula for distance.
def find_r(first_x, first_y, second_x, second_y):
    r = nsimplify(
        sqrt(
            (second_x - first_x)**2 + (second_y - first_y)**2
        )
    )

    print(
        f'r = {r} \nr2 = {r**2}'
    )
# find_r(-9,1,0,0)

# question gives 2 "END" points and neither are the center.
# finds the center using the formula for midpoint
def find_center(first_x, first_y, second_x, second_y):
    center_x = nsimplify((first_x + second_x)/2)
    center_y = nsimplify((first_y + second_y)/2)
    print(f'center = ({center_x}, {center_y})')
    # now that we have center, we can find the radius using it and any previous point. We just use the first.
    find_r(center_x, center_y, first_x, first_y)
# find_center(9,6,-1,4)

x = symbols('x')
h = symbols('h')
f = implemented_function('f', lambda x: 3*x**2 + 2*x -4)
lam_f = lambdify(x, f(x))
# print(nsimplify(simplify(lam_f(x+h))))

def function_1(x):
    function_negativity = 1
    if x == '-x':
        x = (-symbols('x'))
    elif x == 'negative x':
        x = symbols('x')
        function_negativity = -1
    elif x == 'test':
        x = (symbols('x') + symbols('h'))
    else:
        x = int(x)
    return nsimplify( simplify(3*x**2 + 2*x -4) * function_negativity)

# print(
#     function_1(input('>: '))
# )

x = symbols('x')
equation = Eq(
    2*x-8,0
)
# print(
#     solve(equation)
# )

# print(
#     reduce_inequalities(
#         x-2 >= 0
#     )
# )


def is_it_even_or_odd(func, result):
    if func == result:
        return 'even'
    elif func * -1 == result:
        return 'odd'
    else:
        return 'neither'
    
def test_func(x):
    return simplify(4*x**3+5)
# print('test question', test_func(-x))
# print('it is', is_it_even_or_odd(test_func(x),test_func(-x)))


def homework_function(x):
    if x < 0:
        return x**2
    elif x == 0:
        return 2
    elif x > 0:
        return 2*x+4
# 
print(4 * 0.1)

