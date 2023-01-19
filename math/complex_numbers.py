import math
from sympy import *
'''
example 1

x**2 - 14x + 50 = 0
no real solution

sqrt(-1) = letter I = imaginary unit
sqrt(-4) = sqrt(-1 4) = 2I or I2
-1 = I**2

a + bI
4 + 0I | the 4 is the real number, and the 0 is the imaginary

adding | (a + bI) + (c + dI) = add the real and add imag. + (a + c) + (bI + DI)

subtracting | (a + bI) - (c + dI) = (a - c) + (bI - dI)
'''

'''
1) (2 - 3I) + (4 + I)
2) (2 - 3I) - (4 + I)
3) 3I(4 + 10I)
4) (2 - 3)(4 + I)
'''

'''
x**2 + 81 = 0
-9i, 9i
'''

# x = symbols('x')

# equation = Eq(
#     x**2 + 81, 0
# )

# print(solve(equation))



print(
    complex(2, -3) + complex(4, 1)
)