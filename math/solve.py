from sympy import *

# x = symbols('x')

# equation = Eq(
#     x**2-2*x+26,0
# )


# linear
# print(solve(equation))

# print(factor(
#     5*x**2-14*x-3
# ))

# b**2-4ac - the discriminate.

# print(
#     30**2 - 4 * 9 * 25
# )

# reduce inqueatlies
x = symbols('x')

print(
    reduce_inequalities(
        abs(4*x-11)>=6
    )
)

