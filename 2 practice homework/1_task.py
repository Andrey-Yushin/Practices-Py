'''Condition. It is believed that one year lived by a dog is equivalent to seven human years.
This often does not take into account that dogs become completely adult by the age of two.
Thus, many people prefer to equate each of the first two years of a dog's life to 10.5 years of human life,
and all subsequent years to four. Write a program that will convert human age to dog
age, taking into account the logic mentioned above.
Make sure that the program works correctly when calculating the age of a dog less than or more than two years old.'''

x = int(input('Enter the age of the dog: '))

total = 0
for i in range(x):
    if i < 2:
        total += 10.5
    else:
        total += 4
print(f'{x} years = a dogs {total} years')