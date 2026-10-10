def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while(should_continue):
        
        op = input("Pick an operation: ")
        if not op in operations.keys():
            print("Please input a valid operation!")
            break
        num2 = float(input("What's the next number?: "))

        func = operations[op]
        answer = func(num1, num2)

        print(f"{num1} {op} {num2} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart the calculation, or 'q' to exit: ").lower()

        if cont == "y":
            num1 = answer
        elif cont == "n":
            should_continue = False
            calculator()
        elif cont == "q":
            print("Goodbye!")
            break
        else:
            print("Please input a valid answer! Restarting the calculator!")
            calculator()

calculator()