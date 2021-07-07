# Import the logo
from demo import calc_logo
print(calc_logo)

# Define functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2

# define a function called calculate and pass the inputs to calculate
functions = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
    '%' : modulus
}

def calculate():
    num1 = float(input("What is the first number? "))
    # ask the user to select a symbol(+,-, etc) to use for the calculation.
    for symbol in functions:
        print(symbol)

    should_continue = True
    while should_continue:
        calculation_symbol = input("Select the calculation symbol from the list above: ")
        num2 = float(input("input the second number: "))

        calculation = functions[calculation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {calculation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculate()
calculate()

"""
From here, we have 2 options. 
1. Continue and build on the current answer.
2. Clear the calculation and start a new one. 
"""










