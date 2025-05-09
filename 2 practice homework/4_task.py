'''Condition. In this exercise, you will have to develop a program in which the user
will be asked for a list of words until he leaves the input line empty.
After that, the screen should show the words entered by the user, but without repetitions, each one once.
In this case, the words should be displayed in the same order in which they were entered from the keyboard.'''

list = []

while True:
    x = input()
    if x == '': # With an empty input, we stop the cycle.
        break
    elif x not in list:
        list.append(x)

print(list)