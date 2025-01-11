def perform_operation(num1, num2, operation):
    """returns arithmetic operations"""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("You are dividing by zero which is impossible, try another number.")
        else:
            return num1 / num2
