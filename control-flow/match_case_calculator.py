# match_case_calculator.py

# User input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case _ if operation == "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case _ if operation == "-":
        if num1 > num2:
            result = num1 - num2
            print(f"The result is {result}.")
        else:
            result = num2 - num1
            print(f"The result is {result}.")
    case _ if operation == "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case _ if operation == "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
