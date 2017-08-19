from sys import argv
script, first, first1, second, third, surname = argv

print("The script is called:", script)
print("Your first variable is:", first, first1)
print("Your second variable is:", second)
print("Your third variable is:", third)
name = input('Please enter your name --> ')
print(f'Your name is {name} and your surname comes from arguments is --> {surname} ')
