'''Condition. A polygon is called regular if all its sides and angles are equal.
The area of such a shape can be calculated using the following formula,
in which s is the length of the side and n is the number of sides: (n * s**2) // (4 * tan(3.14/n))
Write a program that will ask the user for the values
of the variables s and n and display the area of a regular polygon
based on these values..'''

from math import tan, pi

s = float(input('Enter the length of the side: '))
n = int(input('Enter the number of sides: '))
print('The area of the polygon is %.2f' % ((n * s**2) / (4 * tan(pi / n))))
