def generate_fibonacci(n):
    """
    Generates the first n numbers of the Fibonacci sequence.

    Args:
        n (int): The number of Fibonacci numbers to generate.
                Must be a non-negative integer.

    Returns:
        list: A list containing the first n Fibonacci numbers.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence