
'''Condition. The sieve of Eratosthenes is an algorithm invented more than 2000 years ago and used to find
all prime numbers from 2 to an integer n. Your solution should start by asking the user
to enter a number up to which to output the primes. The description of this algorithm is given below..

###################################################
We write out all integers from 0 to a given boundary
We cross out 0 and 1 as non-simple numbers.
Setting the value of the variable p to 2
As long as p is less than the specified number, we do:
    We cross out all the numbers that are multiples of p, but not its self
    Setting the value of p equal to the next uncrossed number
We output all the numbers that remain uncrossed
###################################################

Write a Python program that implements the above algorithm for displaying prime numbers in the range from two
to the value entered by the user. If the algorithm is implemented correctly,
your program will be able to output all prime numbers from two to a million in just a couple of seconds..'''

x = int(input('Set the border: '))

list = [2] # list of values
p = 2

for _ in range(2, x + 1): # a list from 2 to a given value
    if _ % p != 0 and _ != p: # if the number is a multiple of and not equal to "p"
        list.append(f'{_:,}') # adding it to the list

for i in list:
    print(f'{i}')
