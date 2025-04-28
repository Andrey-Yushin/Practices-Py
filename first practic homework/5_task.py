'''Imagine that you are writing software for an automatic checkout in a self-service store.
One of the functions included in the cash register should be the calculation of the change in case of payment by the buyer in cash.
Write a program that will ask the user for the amount of change in pennies. After that, she must
calculate and display on the screen how many and which coins will be required to issue the specified amount, provided that
the minimum possible number of coins must be involved. Let's say we have coins in
denominations of 1, 5, 10, 50 kopecks, as well as 1, 2 and 5 rubles..'''

rub = 23
kop = 70

list_i = [1, 2, 5] # list of ruble coins
list_rub = [] # list of ruble coins for change
list_f = [1, 5, 10, 50] # the list of kopecks
list_kop = [] # the list of kopecks for change

while len(list_i) > 0: # the list is not empty yet
    a = list_i[-1]  # we take the last element of the list
    if list_i[-1] <= rub: # we check that the last item is more than the amount given by the buyer
        list_rub.append(a) # we add our coin to the deposit list
        rub -= list_i[-1] # we overwrite the change (we subtract the last item of the list from the amount)
    else:
        list_i.pop() # otherwise, we delete the last last item in the list.

while len(list_f) > 0: # the same cycle, only for pennies
    b = list_f[-1]
    if list_f[-1] <= kop:
        list_kop.append(b)
        kop -= list_f[-1]
    else:
        list_f.pop()

# Something like a beautiful conclusion
for rub in set(list_rub):
    print('%d rubles for %d piece' % (rub, list_rub.count(rub)))
for kop in set(list_kop):
    print('%d kopecks for %d piece' % (kop, list_kop.count(kop)))

# Another output option, but perhaps not very convenient.
# print('Ruble coins: ', {rub: list_rub.count(rub) for rub in set(list_rub)})
# print('Kopecks: ', {kop: list_kop.count(kop) for kop in set(list_kop)})