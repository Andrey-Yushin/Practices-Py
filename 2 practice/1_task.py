'''Condition. At the zoo, the price of admission depends on the age of the visitor. Children under two years old are allowed free of charge.
Children between the ages of three and 12 can visit the zoo for 140. For seniors over 65, admission will cost 180,
a regular adult ticket costs 230.
Write a program that will query the age of all the visitors in a group (one at a time)
and display the total price of tickets for visiting the zoo by this group. As an indicator of the end of the input, you can
traditionally use an empty line. The total ticket price should be displayed in the format with two decimal places..'''


tickets = 0 # adult ticket counter
tickets_pensioner = 0
tickets_child = 0

while True:
    x = input('Enter the age of the visitor: ')

    if x == '': # With an empty input, we stop the cycle.
        break
    elif x.isalpha() == True: # checking the number input
        print('Enter the age')
        print('To stop typing, press Enter')
    else: # age verification
        if int(x) >= 65:
            tickets_pensioner += 1 # +1 ticket for a pensioner
        elif 65 > int(x) >= 13:
            tickets += 1 # +1 adult ticket
        elif 12 >= int(x) > 3:
            tickets_child += 1 # +1 kid
        # admission is free for children under 3 years old, they are not counted

# total ticket price (number of people * ticket amount)
total = tickets * 230 + tickets_child * 140 + tickets_pensioner * 65

print('Total ticket price %.2frub' % (float(total)))

