'''The online store sells various souvenirs and trinkets.
Each souvenir weighs 75 g, and the trinket weighs 112 g. Write a program
that asks the user for the number of those and other purchases,
and then display the total weight of the parcel on the screen..'''

souvenir = int(input('Enter the number of souvenirs: '))
trifle = int(input('Enter the number of trinkets: '))
print('Total weight: %dг' % (souvenir * 75 + trifle * 112))