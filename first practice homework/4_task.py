'''Create a program that asks the user for two integers a and b,
and then displays the results of the following mathematical operations:
- sum of a and b;
- the difference between a and b;
- the product of a and b;
- the quotient of dividing a by b;
- the remainder of dividing a by b;
- decimal logarithm of the number a;
- the result of raising the number a to the power of b.'''

import math

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(f'sum of {a} and {b} = ', a + b)
print(f'the difference between {a} and {b} = ', a - b)
print(f'the product of {a} and {b} = ', a * b)
print(f'the quotient of dividing {a} by {b} = ', a // b)
print(f'the remainder of dividing {a} by {b} = ', a % b)
print(f'decimal logarithm of the number {a} = ', math.log10(a))
print(f'the result of raising the number {a} to the power of {b} = ', a**b)