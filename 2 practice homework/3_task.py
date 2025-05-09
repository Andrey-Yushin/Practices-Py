'''Condition. Fizz-Buzz is a famous game that helps children learn division rules in a playful way.
The participants sit in a circle so that the game can theoretically continue indefinitely.
The first player says "One" and passes the move to the one on the left. Each player must mentally add
one to the previous number and pronounce either it or one of the keywords: Fizz, if the number
is completely divisible by three, or Buzz, if by five. If both of these conditions are met, he pronounces Fizz-Buzz.
A player who fails to say the correct word is eliminated from the game. The last remaining player is declared
the winner. Develop a program that implements the Fizz-Buzz game algorithm for the first 100 numbers.
Each subsequent response should be displayed on a new line.'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz-Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)