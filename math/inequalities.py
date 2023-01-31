from sympy import *

'''
set notation
inequality  | numberline        | interval
x < a       | -oo <===0===a---> | (-oo, a)
                all numbers < a
x > a       | <---0---a===> oo
                all numbers > a | (a, oo)
x >= a      | <---0---[a===> oo | [a, oo)

a < x < b   | <--a==0==b-->     | (a, b)

a <= x < b  | <--[==0==b-->     | [a, b)

a>b or x<b  | -oo <==b---a==> oo| (-oo, b) or (a, 00)
'''

'''
examples
#1, x + 8 < 11
#2, 2 - 6 * x <= -4
#3, 7 * x - 11 <= 9 + 2 * x
#4, 6 - 3 * (1 - x) <= 5
(-oo, 2/3] or x <= 2/3
#5, 1/5 * (x - 12) > x + 16
(-oo, -23) or x < -23
'''


x = symbols('x')

print(
    reduce_inequalities(
        (4 < x - 8, x - 8 < 10)
    )
)
'''
'''



'''
compounded inequality
4 < x - 8 < 10

print(
    solve(
        4 < x - 8
    ),
    solve(
        x - 8 < 10
    ),
)

'''


# print(
#     linsolve(
#         [
#             4 < x - 8, x - 8 < 10
#         ], x
#     )
# )