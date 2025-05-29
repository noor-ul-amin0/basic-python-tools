# Basic Python Tools (Easy Assignment)

This directory contains simple Python modules that perform basic operations. Each module focuses on a specific functionality and demonstrates core Python concepts.

## Modules

### Calculator (`calculator.py`)

A basic calculator that performs arithmetic operations.

- Takes two numbers and an operator (+, -, \*, /) as input
- Returns the result of the calculation
- Handles division by zero errors

**Example:**

```python
result = calculate(5, 3, "*")  # Returns 15
```

### Temperature Converter (`temperature_converter.py`)

Converts temperatures between Celsius and Fahrenheit.

- Functions for both Celsius to Fahrenheit and Fahrenheit to Celsius
- Formats the output with appropriate units

**Example:**

```python
result = convert_temperature(25, "Celsius")  # Returns "77.0 Fahrenheit"
```

### Vowel Counter (`vowel_counter.py`)

Counts the number of vowels (a, e, i, o, u) in a given string.

- Case-insensitive (counts both uppercase and lowercase vowels)

**Example:**

```python
count = count_vowels("Hello, world!")  # Returns 3
```

### List Operations (`list_operations.py`)

Performs common operations on lists.

- Calculate sum of a list
- Calculate average of a list
- Find maximum value in a list
- Reverse a list

**Examples:**

```python
numbers = [1, 5, 3, 8, 2]
sum_result = calculate_sum(numbers)  # Returns 19
avg_result = calculate_average(numbers)  # Returns 3.8
max_result = find_maximum(numbers)  # Returns 8

my_list = ['a', 'b', 'c']
reversed_list = reverse_list(my_list)  # Returns ['c', 'b', 'a']
```

## Running the Examples

You can run all examples by executing the main.py script:

```bash
python main.py
```

This will demonstrate all the functionality with sample inputs and outputs.

## Requirements

- Python 3.x
- No external dependencies
