from art import logo
from replit import clear

# Calculator


# Add
def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


# Substract
def sub(a, b):
    """Returns the substraction of two numbers"""
    return a - b


# Multiply
def multiply(a, b):
    """Returns the multiplication of two numbers"""
    return a * b


# Divide
def divide(a, b):
    """Returns the divisibility of two numbers"""
    return a / b


def do_operations(n1, n2, op):
    """Execute the input operation between two inputs numbers"""
    operations = {'+': add, '-': sub, '/': divide, '*': multiply}
    return operations[op](n1, n2)


def calculator():
    clear()
    print(logo)
    first_number = float(input("What's the first number?: "))

    continue_calculation_result = True
    while continue_calculation_result:
        operation = input("+ \n- \n* \n/ \nPick an operation: ")
        while not operation in ['+', '-', '*', '/']:
            operation = input(
                "Operation is not valid, try again\n+ \n- \n* \n/ \nPick an operation: "
            )

        second_number = float(input("What's the next number?: "))

        result = do_operations(first_number, second_number, operation)

        print(f"{first_number} {operation} {second_number} = {result}")

        input_should_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        )
        while not input_should_continue in ['y', 'n']:
            input_should_continue = input(
                f"Input is not valid, try again\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
            )

        if input_should_continue == 'y':
            first_number = result
        else:
            continue_calculation_result = False
            calculator()


calculator()
