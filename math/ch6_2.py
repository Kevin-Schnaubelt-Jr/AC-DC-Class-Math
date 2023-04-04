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


'''
a**b = x

logarithm: Rewritten exponential expression.
loga(x) = b
2 is base, 3 is exponent, 8 is argument
log2(8) = 3

example:
rewrite in log form
1. 49 = 7**2
2. a**7 = 2.1
3. e**x = 20

1. log7(49) = 2
2. loga(2.1) = 7
3. loge(20) = x
'''

'''
natural logarithm. Logarithm with base e. loge(x) = b IS ln(x) = b

let's try some
1. e**x = 3
2. 27 = 3**3
3. a**y = 5

1. ln(3) = x
2. log3(27) = 3
3. loga(5) = y
'''

'''
logarithm functions: Inverse of exponential functions. f(x) = a**x
lets graph it.
first off, a > 1, the graph will be increasing.
the domain is (-oo,oo)
the range H,A or y = 0. (0,oo) or y > 0

the log function is the inverse of the exponential function.
f(x) = a**x = loga(x)
so the points are mirrored. So flip the x and y values of the points.
vertical asymptotes are at x = 0.
switch the domain and range.
domain is (0,oo) or x > 0
range is (-oo,oo).


example: f(x) = log2(x)
graph it
what are the domain, range, and vertical asymptotes?
we know that this is = to f(x) = 2**x
so the points are:
(1,0)
(2,1)
(1/2,-1)

the normal exponential function domains and range are:
domain: (-oo,oo)
range: (0,oo) or y > 0

the logarithmic function domains and range are:
domain: (0,oo) or x > 0
range: (-oo,oo)
'''

'''
f(x) = ln(x)
so for f(x) = e**x
the points are:
(0,1)
(1,e)
(-1,1/e)

for ln(x)
the points are:
(1,0)
(e,1)
(1/e,-1)


lets do an example: 
graph f(x) = ln(x-1)
start with f(x) = ln(x)
so the points will be:
(1/e,-1)
(1,0)
(e,1)
domain is (0,oo) or x > 0 A,A
range is (-oo,oo)

because of x-1, there is a horizontal shift. So shift right because of the minus
so the points will be:
(1/e+1,-1)
(2,0)
(e+1,1)
the new vertical asymptote is at x = 1
the new domain is (1,oo) or x > 1
the range stays the same (-oo,oo)

so, f(x) = ln(x-1) shifted right 1 unit.
f(x) = ln(x+1) shifted left 1 unit.
f(x) = ln(x) - 1 shifted down 1 unit.
f(x) = ln(x) + 1 shifted up 1 unit.
'''

'''
example: graph f(x) = ln(x+4)
start with f(x) = ln(x)
so the points will be:
(1/e,-1)
(1,0)
(e,1)
domain is (0,oo) or x > 0 V,A
range is (-oo,oo)

because of x+4, there is a horizontal shift. So shift left because of the plus
so the points will be:
(1/e-4,-1)
(-3,0)
(e-4,1)
the new vertical asymptote is at x = -4
the new domain is (-4,oo) or x > -4
the range stays the same (-oo,oo)
'''

'''
extra spice
finding an inverse function
step 1: write y = blank
step 2: switch x and y
step 3: solve for y
step 4: replace y with f**-1(x)

so if f(x) = cbrt(x+2)
so y = cbrt(x+2)
x = cbrt(y+2)
cube both sides, so x**3 = cbrt(y+2)**3
which would equal x**3 = y + 2
so x**3 - 2 = y
'''