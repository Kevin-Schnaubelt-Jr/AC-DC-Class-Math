from sympy import *

'''
topics
'''

'''
exponent rules:
1) a1 = a
2) a**0 = 1, but 0**0 is undefined
3) am/an = a*m-n
4) a**m * a**n = a*m+n
5) (1/b)**n = (a**n)/(b**n)
6) (a/b)**-n = (b/a)**n
7) a**-n = 1/(a**n)
8) (a**m)**n = a**m*n
9) a**u = a**v
then u=v
'''

'''
examples:
2**-x = 4
(3/2)**x = 27/8
2**(2x+1) = 4

for the first one, make 4 into 2**2. then you can do 
'''

'''
(3/2)**x = 27/8
2**(2*x+1) = 4
4**(x**2-8) = 16**x
e**x = e**(3*x+10)
Make not of e, because it will show up a lot.
e = 2.718281828459045
'''
x = Symbol('x')

equation = Eq((3/2)**x,27/8)

print(nsimplify(solve(equation)[0]))

equation_2 = Eq(2**(2*x+1),4)

print('equation_2',nsimplify(solve(equation_2)[0]))

# the answer to this should be 4 and -2
equation_3 = Eq(4**(x**2-8),16**x)


print('equation_3',nsimplify(solve(equation_3)[0]))

equation_4 = Eq(E**x,E**(3*x+10))

print('equation_4',nsimplify(solve(equation_4)[0]))

'''
topic 2, exponential functions.
so f(x) = a**x
if a > 1 the graph will be increasing
if 0 < a < 1 the graph will be decreasing
never crosses the x axis
asympototes are horizontal lines at y = 0
(H,A)

the domain are the x values. (-oo,oo)
the range are the y values. (0,oo) or y > 0


main points
(0,1)
(1,a)
(-1,1/a)

'''

'''
example 1: f(x) = 3**x
graph it
what are the domain, range, and horizontal asymptotes?

the graph is increasing
domain: (-oo,oo)
range: (0,oo) or y > 0
horizontal asymptotes: y = 0
'''

'''
transformation (translation)
this will shift the graph up or down or left or right.
so for f(x) = 3**x+2, this is a shift up 2 units.

for f(x) = 3**x-2, this is a shift down 2 units.

for f(x) = 3**x-2, go right 2 units.
and for f(x) = 3**x+2, go left 2 units.
'''

'''
example 2: f(x) = 5**x + 1
graph it
what are the domain, range, and horizontal asymptotes?

so because it shifts up 1, the mains points will be:
(0,2)
(1,5)
(-1,6/5) or (-1,1+1/5)

because it shifts up 1, the new horizontal asymptote is y = 1
so the range is now (1,oo) or y > 1
domain stays the same (-oo,oo)
'''

'''
example 3: f(x) = 3**(x-2)
graph it
what are the domain, range, and horizontal asymptotes?

because it shifts right 2, the mains points will be:
(2,1)
(3,3)
(1,1/3)

because it shifts right 2, the new horizontal asymptote is y = 2
the range stays the same, because there is no shift up or down.
domain stays the same (-oo,oo)
'''