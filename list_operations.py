\
def calculate_sum(numbers):
    """Calculates the sum of a list of numbers."""
    return sum(numbers)

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0  # Or raise an error, depending on desired behavior for empty list
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    """Finds the maximum value in a list of numbers."""
    if not numbers:
        return None  # Or raise an error
    return max(numbers)

def reverse_list(data_list):
    """Reverses the elements of a list."""
    return data_list[::-1]
