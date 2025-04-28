'''Imagine that you have opened a savings account with a bank at 4% per annum.
The bank calculates the interest at the end of the year and adds it to the invoice amount.
Write a program that asks the user for the amount of the initial deposit,
after which it calculates and displays the amount on the account at the end of the first, second and third years.
All amounts must be rounded to two decimal places..'''

n = int(input())
for i in range(3):
    pr = n * 0.04
    n = n + pr
    print(f'For {i+1} year: %.2f rub' % (n))
