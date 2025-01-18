def safe_divide(numerator, denominator):
    """function that performs division."""
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    except ValueError:
        return f"Error: Please enter numeric values only."
