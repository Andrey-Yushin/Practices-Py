'''Condition. Write a program that will ask the user for numbers until an empty string is entered.
First, the average value of the entered series of numbers should be displayed on the screen, after that, one after another, it is necessary
to display a list of numbers below the average, equal to it (if any) and above the average.
Each list should be preceded by a corresponding heading.'''

list = [] # list of numbers
low = [] # The list of numbers is below average
high = [] # A list of above-average numbers

while True:
    x = input('Enter a number: ')
    if x == '': # if an empty string is entered
        break
    else:
        try: # adding a number to the list
            list.append(int(x))
        except ValueError:
            print('Enter a number!')
            print('To stop typing, press "Enter"')

total = 0 # the sum of all the numbers
for i in list:
    total += i

average = total / len(list) # average

for _ in list:
    if _ <= average: # if the number of the list is less than the average
        low.append(_) # adding it to the 'smaller' list
    else:
        high.append(_) # otherwise, to the 'high' list

print(f'The arithmetic mean of the numbers is: {average}')
print()
print('The numbers are less than average:')
for l in low:
    print(l)
print('The numbers are above average:')
for h in high:
    print(h)
