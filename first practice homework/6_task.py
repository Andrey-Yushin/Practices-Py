'''The bakery sells bread for 49 rubles per loaf. The discount on yesterday's bread is 60%.
Write a program that will ask the user for the number of loaves of bread purchased yesterday.
The display should include the regular price per loaf, the discounted price, and the total cost of the purchased bread.
All values should be displayed on separate lines with appropriate descriptions.
Use the format with two decimal places and 5 decimal places for the output..'''

n = int(input('Enter the number of rolls you bought yesterday: '))
cost = 49

print('Price per loaf %.2f rub' % (cost))
print('Discounted price %.2f rub' % (cost - (cost * 0.6)))
print('The total cost of the discount %.2f rub' % ((cost - (cost * 0.6)) * n))
