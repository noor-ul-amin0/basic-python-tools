\
def count_vowels(input_string):
    """
    Counts the number of vowels in a string.

    Args:
        input_string: The string to count vowels in.

    Returns:
        The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
