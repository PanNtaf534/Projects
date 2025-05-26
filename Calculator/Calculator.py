from Calculator_Art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("Type in your first number: "))
    should_continue = True

    while should_continue:
        math_op = input("\n '+' \n '-' \n '*' \n '/' \nPick a mathematical operator:  ")
        if math_op not in operations:
            print("Wrong input.")
            continue
        num2 = float(input("Type in your second number: "))


        result = operations[math_op](num1,num2)
        print(f"{num1} {math_op} {num2} = {result}")

        user_choice = input("Press 'y' to go again with the previous result as the first number,press 'n' to start over.").lower()

        if user_choice == 'y':
            num1 = result
            print(f"Previous result: {num1}")
        elif user_choice == 'n':
            print("\n"*20)
            calculator()
            return
        else:
            print("Invalid input. Exiting program.")
            should_continue = False

calculator()