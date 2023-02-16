from sympy import *

'''
y=3x+4
they want the slope, y intercept, and graph the line.

y=mx+b (b is the y intercept)

m=3 and intercept = 4.
so the slope is 3.
y intercept is 4

for the graph, plot (0,4)
slope is rise divided by 1. 3=3/1. so go up 3 and over 1. so (1,7)
'''

'''
find equation of the line. answer in slope intercept form = y=mx+b

example:
find the equation of a line that goes through (2,4) and (4,3)

m = second y - first y / second x - first x which is 3-4/4-2 which is -1/2
so y = -1/2 * x + b

take one of the points, doesn't matter which and do this: for points (2,4) do 4 = -1/2 * 2 + b
b = 5

so y = -1/2 * x + 5
'''

'''
example 2
(-1,-2) and (-3,7)

'''

def line_intercept_form(first, second):
    first_point = first
    second_point = second
    M = f'{(second_point[1] - first_point[1])} / {(second_point[0] - first_point[0])}'
    M_number = (second_point[1] - first_point[1]) / (second_point[0] - first_point[0])
    # print(M)
    b = symbols('b')
    B = solve(
        Eq(
            first_point[1], M_number * first_point[0] + b
        )
    )
    # print(int(B[0]))
    print(
        f'y = {M} * x + {int(B[0])}'
    )

# line_intercept_form()

'''
parallel / perpendicular lines 

parallel lines that dont intersect. need same slope M but different y intercepts. so a different b.

perpendicular lines form right angles, so four 90 degree angles. slopes are called negative reciprocals.
so M=3 and M=-1/3 are negative reciprocals.

3 is the same as 3/1. so invert to 1/3 and change the sign, -1/3

y = -1/3x - 4
find the parallel will be M=-1/3 (just put -1/3)
find the perpendicular will be M=3 (just put 3)
'''

'''
parallel if slopes are equal 1st M and 2nd M
perpendicular if slopes are negative reciprocals 1st M = -1/2nd M

example given y=3*x parallel
point (-2,3)
so 3 = 3*(-2) + b
b = 9

answer is y = 3*x + 9

y=3*x perpendicular
(-2,3)
negative reciprocal for the M, so -1/3
so y = -1/3 * x + b
find be by doing 3 = -1/3 * (-2) + b
b = 7/3

y = -1/3 * x + 7/3
'''

'''
find equation of a line parallel to y= -1/3 * x + 3 parallel
points (1,3)

answer y = -1/3 * x + 10/3

find equation of a line y = -2/5 * x -4 perpendicular
points (2,5)

y = 5/2 * x + 0
'''

def parallel_find():
    b = symbols('b')
    y = 3
    x = 1
    m = (-1/3)
    equation = Eq(
        y, m*x + b
    )
    print(
        solve(
            equation
        )
    )
parallel_find()

def perpendicular_find():
    b = symbols('b')
    y = 5
    x = 2
    m = ['-','2','5']
    if m[0] == '-':
        m_negative_reciprocal = (int(m[2]) / int(m[1]))
    else:
        m_negative_reciprocal = (-int(m[2]) / int(m[1]))
    equation = Eq(
        y, m_negative_reciprocal *x + b
    )
    print(
        solve(
            equation
        )
    )
perpendicular_find()


'''
point slope form
y - 1st y = M (x - 1st x)

slope = 3
point (1,5)
answer: y-5=3(x-1)
'''