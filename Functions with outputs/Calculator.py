from logo import logo


#! Add
def add(n1, n2):
    return n1 + n2

#! Subtract
def subtract(n1, n2):
    return n1-n2

#! Multiply
def multiply(n1, n2):
    return n1*n2

#! Divide
def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first Number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        # answer = 0
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number"))
        calculation_function = operations[operation_symbol]
        print(calculation_function)
        answer = calculation_function(num1, num2)
        # print(answer)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculating with {answer}: "):
            num1 = answer
        else:
            should_continue = False
            calculator()

        # operation_symbol = input("Pick another operation: ") 
        # num3 = int(input("What's the next number?"))
        # calculation_fucntion = operations[operation_symbol]
        # second_answer = calculation_function(answer, num3)
        # print(f"{answer} {operation_symbol} {num3} = {second_answer}")

calculator()










