'''Condition. Write a program that asks the user for a number and calculates the sum
of positive natural numbers from 1 to the value entered by the user.
The sum of the first n positive numbers can be calculated using the formula: sum = n * (n+1)  // 2'''

n = int(input('Enter a positive natural number: '))
a = n * (n+1) // 2
print('the sum of the first %d positive numbers is %d ' % (n, a))
