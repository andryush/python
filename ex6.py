types_of_people = 10 # 1 var
x = f'There are {types_of_people} types of people.' #format string inputinq  1 var

binary = 'binary' # 2 var
do_not = 'don\'t' # 3 var
y = f'Those who know {binary} and those who {do_not}.' #format string inputing 2 & 3 var, 1

print(x) # printing line 2
print(y) # printing line 6

print(f'I said: {x}') # format string inputing x var, 2
print(f'I also said: "{y}"') # format string inputing y var, 3

hilarious = False # var 4
joke_evaluation = 'Isn\'t that joke so funny?!, {}' # don't forget to put empty brackets for including var with var.format

print(joke_evaluation.format(hilarious))  #format string with var.format(var name), 4

w = 'This is a left side of...' # var w
e = 'a string with a right side.' # var e

print(w + e) # joining 2 strings with print
