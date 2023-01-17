from sympy import *

x = symbols('x')

equation = Eq(
    x**2 - 4, 0
)


# linear
print(solve(equation))

# print(factor(
#     5*x**2-14*x-3
# ))
