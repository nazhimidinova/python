def addition(x, y):
    sum = x + y 
    return sum

def subtraction(x, y):
    difference = x - y
    return difference

def multiplication(x, y):
    product = x * y
    return product

def division(x, y):
    if y == 0:
        print('ZeroDivisionError. Please try again: ')
        return None
    quotient = x / y
    return quotient

def calculator():
    print('Welcome to the calculator program!')
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    inp1 = input('Enter the operator (+, -, *, /): ')

    if inp1 == '+':
        result = addition(x, y)
    elif inp1 == '-':
        result = subtraction(x, y)
    elif inp1 == '*':
        result = multiplication(x, y)
    elif inp1 == '/':
        result = division(x, y)
    else:
        print('Wrong character. Try again: ')
        return None

    print('Result:', result)

calculator()


