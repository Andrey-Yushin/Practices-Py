'''Condition. To win the main prize, it is necessary that the six numbers on the lottery ticket match the six numbers
that randomly appeared in the range from 1 to 49 during the next draw.
Write a program that will randomly select six numbers for your ticket.
Make sure that there are no duplicates among these numbers. Display the ticket numbers on the screen in ascending order.'''

import random

random_list = []

while len(random_list) < 5:
    x  = random.randint(1, 49)
    if x not in random_list:
        random_list.append(x)
    else:
        continue

print(random_list)