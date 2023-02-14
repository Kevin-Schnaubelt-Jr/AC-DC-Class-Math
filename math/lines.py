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

def line_intercept_form():
    first_point = 2,4
    second_point = 4,3
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