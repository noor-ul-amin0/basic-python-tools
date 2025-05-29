# Python Advanced Tools (Medium Assignment)

This directory contains more advanced Python modules that build upon fundamental concepts and demonstrate more complex functionality.

## Modules

### Fibonacci Sequence (`fibonacci_sequence.py`)

Generates the Fibonacci sequence up to a specified number of terms.

- Validates input to ensure it's a non-negative integer
- Handles edge cases (n = 0, n = 1)

**Example:**

```python
sequence = generate_fibonacci(8)  # Returns [0, 1, 1, 2, 3, 5, 8, 13]
```

### Word Frequency Counter (`word_frequency.py`)

Reads text from a file and counts how frequently each word appears.

- Uses regular expressions to identify words
- Handles file errors gracefully

**Example:**

```python
# For a file containing: "This is a test. This is only a test."
frequencies = count_word_frequency("filename.txt")  # Returns {'This': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
```

### Data Validation (`data_validation.py`)

Validates user input against different data types.

- Supports integers, floats, email addresses, dates, and phone numbers
- Returns boolean result indicating whether the input is valid for the specified type

**Example:**

```python
is_valid = validate_input("5", "integer")  # Returns True
is_valid = validate_input("user@example.com", "email")  # Returns True
```

### File Handling (`file_handling.py`)

Contains two main components:

1. **Student Grade Calculator**

   - Reads a CSV file containing student grades
   - Calculates the average grade for each student

   **Example:**

   ```python
   averages = calculate_student_averages("student_grades.csv")
   # Returns {'Alice': 89.5, 'Bob': 86.25, ...}
   ```

2. **Address Book**

   - A class for managing contacts
   - Store name, phone, email, and address
   - Add, search, and delete contacts
   - Persistence through JSON file storage

   **Example:**

   ```python
   address_book = AddressBook()
   address_book.add_contact("Alice", "555-1212", "alice@example.com")
   result = address_book.search_contact("Alice")
   ```

## Running the Examples

You can run demonstrations of all modules by executing:

```bash
python main.py
```

The script will run through examples of each functionality with sample inputs.

## Requirements

- Python 3.x
- No external dependencies
