numbers = []
def loop(i, j, k):
    while i < j:
        print('\nI at the TOP =', i)
        numbers.append(i)
        print('Numbers now ', numbers)
        i = i + k
        print('I at the Bottom =', i)

loop(0, 5, 1)

print('The numbers:')
for num in numbers:
    print(num)
