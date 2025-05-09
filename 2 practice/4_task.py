'''Condition. Write a program that determines and displays the number of unique characters in
a string entered by the user. For example, in the line Hello, World! It contains ten unique characters, and the zzz string contains one.
Use a dictionary to solve this problem.'''

string = 'Hello, World!'
dict = {}

for char in string:
    dict[char] = 0

print(f'the string contains {len(dict)} characters')
