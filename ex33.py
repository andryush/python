i = 0
numbers = []

while i < 6:
    print(f'At the TOP i = {i}')
    numbers.append(i)
    print('numbers now', numbers)
    i = i + 1;
    print(f'At the bottom i = {i}')

print('The numbers: ')

for num in numbers:
    print(num)
