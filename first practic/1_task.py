''' Condition. In many countries, a certain deposit is included in the cost of glass
containers to encourage beverage buyers to hand over empty bottles.
Let's say bottles with a volume of 1 liter or less cost $0.10, and bottles with a larger volume cost $0.25.
Write a program that asks the user for the number of bottles of each size.
The screen should display the amount that can be saved if you hand over all the available dishes.
Format the output so that the amount includes two decimal places and is complemented by a dollar symbol on the left.. '''

small_bottles = int(input('Enter the number of bottles less than 1 liter: '))
big_bottles = int(input('Enter the number of bottles of more than 1 liter: '))
print('You will receive: $%.2f' % (small_bottles * 0.1 + big_bottles * 0.25))


