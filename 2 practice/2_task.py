'''Write a program that will ask the user for integer values and save them as a list.
Zero should serve as an indicator of the end of entering values. Then the program should display all the numbers entered
by the user (except zero) in ascending order, one value per line.
Use the sort method for sorting.'''


nums = [] # list of numbers

while True:
    x = input('Enter an integer (0 to complete the input): ')

    if x == '0':  # When entering zero, we stop the cycle.
        break
    elif x.isdigit() == True:  # checking the number input
        nums.append(x) # adding the number to the list
    else:
        print('Enter a number')
        print('To stop typing, enter 0')

nums.sort()
for _ in nums:
  print(_)