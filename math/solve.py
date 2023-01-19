from sympy import *

x = symbols('x')

equation = Eq(
    25 * x**2 - 10 * x + 1, 0
)


# linear
print(solve(equation))

# print(factor(
#     5*x**2-14*x-3
# ))

# b**2-4ac - the discriminate.

# print(
#     30**2 - 4 * 9 * 25
# )

