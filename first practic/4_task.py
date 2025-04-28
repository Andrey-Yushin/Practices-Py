'''Condition. You will have to write a program in which the user will enter a time interval
in the form of a total number of seconds, after which the screen should show the same duration
in the format D HH:MM:SS, where D, HH, MM and SS are the number of days, hours, minutes and seconds, respectively.
In this case, the last three values should be output in a two-digit format, as we are used to seeing
them on electronic watches. Try to find out for yourself which characters need to be entered into the format specifier
so that, if necessary, the numbers are supplemented on the left with zeros instead of spaces. In the real practice of a developer,
working with the date and time format is one of the most frequent tasks..'''

n = int(input('Enter the number of seconds: '))
sec_in_day = 86400
sec_in_min = 60
sec_in_hour = 3600
hours_in_day = 24
days = n // sec_in_day
hours = n // sec_in_hour % hours_in_day
minutes = n // sec_in_min % sec_in_min
seconds = n % sec_in_min
print('Time: %dd %02dh:%02dm:%02ds.' % (days, hours, minutes, seconds))
