def add(a, b):
    print(f'ADDING {a} + {b}')
    return a + b

def subtract(a, b):
    print(f'SUBTRACTING {a} - {b}')
    return a - b

def multiply(a, b):
    print(f'MULTYPLING {a} * {b}')
    return a * b

def divide(a, b):
    print(f'DIVIDING {a} / {b}')
    return a / b

print("Let's do some math with just functions!")

age = add(10, 20)
height = subtract(200, 29)
weight = multiply(35, 2)
iq = divide(200, 2)

print(f' AGE: {age}\n WEIGHT: {weight}\n HEIGHT: {height}\n IQ: {iq}')

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
