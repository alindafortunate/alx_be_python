def perform_operation(num1, num2, operation):
    """returns arithmetic operations"""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        try:
            return num1 // num2
        except ZeroDivisionError:
            print("You are dividing by zero which is impossible, try another number.")
