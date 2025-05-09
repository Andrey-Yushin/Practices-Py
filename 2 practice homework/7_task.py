'''Condition. In the famous Scrabble game, each letter has a certain number of points.
The total amount of points that the player who composed this word receives is made up of points for each letter
that is part of it. The more commonly used a letter is in a language, the fewer points are awarded for its use.
Write a program that calculates and displays the number of points per collected word.
Create a dictionary to store the correspondences between letters and points and use it in your solution.
The points system in the Scrabble game:
1 - A, E, I, L, N, O, R, S, T и U
2 - D и G
3 - B, C, M и P
4 - F, H, V, W и Y
5 - K
8 - J и X
10 - Q и Z'''

word = 'Hello World' # the invoice line

char = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
        'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
        'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

list = []

total = 0 # letter counter
for symbol in word.upper().replace(' ',''): # make the letters big and remove the spaces
    total += char[symbol] # counting the amount
    print(f'Character {symbol} = {char[symbol]} points')
print(f'Total amount of points: {total} points')
