def calculator():
    while True:
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'exit' to quit:")

        user_input = input(": ")
        if user_input == "exit":
            break
        elif user_input in ("+", "-", "*", "/"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "+":
                result = num1 + num2
                print("The result is: {result}")
            elif user_input == "-":
                result = num1 - num2
                print("The result is: {result}")
            elif user_input == "*":
                result = num1 * num2
                print("The result is: {result}")
            elif user_input == "/":
                if num2 != 0:
                    result = num1 / num2
                    print("The result is: {result}")
                else:
                    print("Invalid input")