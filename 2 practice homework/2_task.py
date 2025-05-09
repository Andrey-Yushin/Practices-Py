'''Condition. The cells on the chessboard are identified by a letter and a number.
The letter defines the horizontal position of the cell, and the number defines the vertical position, as shown in the figure.
Your program should ask the user for the coordinates of the cell.
Use a conditional expression to determine which cell – white or black – the column starts with.
Then, using ordinary arithmetic, it is necessary to determine the color of a particular cell. For example, if the user enters a1,
the program should determine that the cell with these coordinates is black. If d5 is white.'''


cell = input('Enter the cell number: ')
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # список клеток из букв

if cell[0] in list:
    num = list.index(cell[0]) + 1 # we calculate the letter cell number
    print('Square is black' if (num + int(cell[1])) % 2 == 0 else 'Square is white')
else:
    print('Incorrect input format')
    print('Input example: d5')

