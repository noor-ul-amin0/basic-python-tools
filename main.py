
from calculator import calculate
from temperature_converter import convert_temperature
from vowel_counter import count_vowels
from list_operations import calculate_sum, calculate_average, find_maximum, reverse_list

if __name__ == "__main__":
    # Calculator example
    print("Calculator Example:")
    result = calculate(5, 3, "*")
    print(f"5 * 3 = {result}")
    result = calculate(10, 0, "/")
    print(f"10 / 0 = {result}")
    print("\n")

    # Temperature Converter example
    print("Temperature Converter Example:")
    converted_temp = convert_temperature(25, "Celsius")
    print(f"25 Celsius = {converted_temp}")
    converted_temp = convert_temperature(77, "Fahrenheit")
    print(f"77 Fahrenheit = {converted_temp}")
    print("\n")

    # Vowel Counter example
    print("Vowel Counter Example:")
    vowel_count = count_vowels("Hello, world!")
    print(f"Number of vowels in 'Hello, world!': {vowel_count}")
    print("\n")

    # List Operations examples
    print("List Operations Examples:")
    numbers = [1, 5, 3, 8, 2]
    print(f"Original list: {numbers}")
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")

    my_list = ['a', 'b', 'c']
    print(f"Original list: {my_list}")
    reversed_list_data = reverse_list(my_list)
    print(f"Reversed list: {reversed_list_data}")
