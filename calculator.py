def calculate(num1, num2, operator):
    """
    Performs a calculation based on two numbers and an operator.

    Args:
        num1: The first number.
        num2: The second number.
        operator: The operator (+, -, *, /).

    Returns:
        The result of the calculation.
        Returns an error message if the operator is invalid or division by zero occurs.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"
