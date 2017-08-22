def cheese_and_crackers(cheese_count, crackers_count):
    print(f'You have {cheese_count} cheese')
    print(f'You have {crackers_count} crackers')
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print('We can give numbers to function directly')
cheese_and_crackers(30, 70)

print('Or we can use variables from our script in the function')

cheese_amount = 50
crackers_amount = 50

cheese_and_crackers(cheese_amount, crackers_amount)

print('We can do math inside functions args')
cheese_and_crackers(10 + 7, 33 + 7)

print('Even we can combine variables and math in the function')
cheese_and_crackers(cheese_amount + 30, crackers_amount + 30)
