from sympy import *

'''
absolute value |u|=a which means u can be = a or -a
|3| = 3 and |-3| = 3. It's just the distance from 0.

|3x|=9
which is 3x = 9 or 3x = -9
so x = 3 or x = -3


|4 * x + 2| = 6
x = 1 or x = -2


|5 * x - 1| = 4
5 * x - 1 = 4 or 5 * x - 1 = -4
+ 1
5x = 5 or x = -3
'''
'''
abs(u) < a mean -a < u < a or (u > -a AND u < a)
abs(u) <= a means -a <= u <= a
abs(u) > a means u > a || u < -a
abs(u) >= a means u >= a || u <= -a

expres your answer as an inequality. number and interval. 
set notation inequality = a < x < b
interval = (a,b)

U can mean or
'''
'''
abs(6x) < 36
-6 < x < 6

2. abs(2x+1) >= 5
2 <= x OR x <= -3

3. abs(x) - 4 <= 6
-10 <= x <= 10

4. abs(3 - 2x) + 1 >8
5 < x | x < -2
'''


x = symbols('x', real=True)

# equation= Eq(
#     abs(6 * x), 36
# )



# print(
#     solve(
#         equation
#     )
# )

'''
1. | 4x - 10| >= 7
17/4 < = x or x <= 3/4

2. | 3x | - 8 < 12
-20/3 < x && x < 20/3

3. 5 + | x - 1 | > 1/4
True
(-oo,oo)

absolute value always becomes positive or zero. 
positive numbers > negative numbers which is True

hypothetically | x - 1| < -19/4 is no solution
positive < negative is False or !True

'''
print('-----')
print(
    reduce_inequalities(
            6 + abs(x - 3) > 3/7
        )
)