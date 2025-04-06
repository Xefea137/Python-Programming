"""
In the Python math module there is the function sqrt, which calculates the square root of a number. You can use it like so:
from math import sqrt
print(sqrt(9))

This should print out
3.0

Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:
x = (-b ± sqrt(b²-4ac))/(2a).

You can assume the equation will always have two real roots, so the above formula will always work.
An example of expected behaviour:
Value of a: 1
Value of b: 2
Value of c: -8

The roots are 2.0 and -4.0
"""

from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

root1 = ((-b + (sqrt((b**2) - (4*a*c)))) / (2 * a))
root2 = ((-b - (sqrt((b**2) - (4*a*c)))) / (2 * a))
print(f"The roots are {root1} and {root2}")