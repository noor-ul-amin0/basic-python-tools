from fibonacci_sequence import generate_fibonacci
from word_frequency import count_word_frequency
from data_validation import validate_input
from file_handling import calculate_student_averages, AddressBook
import os

def test_fibonacci():
    """Test the Fibonacci sequence generator."""
    print("\n===== Fibonacci Sequence =====")
    try:
        result = generate_fibonacci(8)
        print(f"First 8 Fibonacci numbers: {result}")
        
        result = generate_fibonacci(1)
        print(f"First 1 Fibonacci number: {result}")
        
        result = generate_fibonacci(2)
        print(f"First 2 Fibonacci numbers: {result}")
        
        try:
            result = generate_fibonacci(-1)
            print(f"Invalid input (-1): {result}")
        except ValueError as e:
            print(f"Invalid input (-1): {e}")
            
    except Exception as e:
        print(f"Error in Fibonacci test: {e}")

def test_word_frequency():
    """Test the word frequency counter."""
    print("\n===== Word Frequency Counter =====")
    try:
        # Create a test file
        test_file = "test_text.txt"
        with open(test_file, "w") as f:
            f.write("This is a test. This is only a test.")
            
        frequencies = count_word_frequency(test_file)
        print(f"Word frequencies: {frequencies}")
        
        # Clean up
        os.remove(test_file)
        
    except Exception as e:
        print(f"Error in word frequency test: {e}")

def test_data_validation():
    """Test the data validation functions."""
    print("\n===== Data Validation =====")
    try:
        test_cases = [
            ("5", "integer"),
            ("5.5", "float"),
            ("not-an-int", "integer"),
            ("user@example.com", "email"),
            ("invalid-email", "email"),
            ("555-1234", "phone"),
            ("2023-05-15", "date")
        ]
        
        for value, data_type in test_cases:
            result = validate_input(value, data_type)
            print(f"Value: '{value}', Type: '{data_type}', Valid: {result}")
            
    except Exception as e:
        print(f"Error in data validation test: {e}")

def test_student_grades():
    """Test the student grade calculator."""
    print("\n===== Student Grade Calculator =====")
    try:
        # Create a test CSV file
        test_file = "student_grades.csv"
        with open(test_file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Student", "Math", "Science", "English", "History"])
            writer.writerow(["Alice", "90", "85", "95", "88"])
            writer.writerow(["Bob", "78", "92", "85", "90"])
            writer.writerow(["Charlie", "88", "91", "87", "85"])
            
        averages = calculate_student_averages(test_file)
        print("Student averages:")
        for student, avg in averages.items():
            print(f"{student}: {avg}")
            
        # Clean up
        os.remove(test_file)
        
    except Exception as e:
        print(f"Error in student grades test: {e}")
        
def test_address_book():
    """Test the address book functionality."""
    print("\n===== Address Book =====")
    try:
        # Use a test file to avoid modifying any real address book
        test_file = "test_address_book.json"
        address_book = AddressBook(test_file)
        
        # Add contacts
        address_book.add_contact("Alice", "555-1212", "alice@example.com", "123 Main St")
        address_book.add_contact("Bob", "555-3434", "bob@example.com")
        address_book.add_contact("Charlie", "555-6789")
        
        # Search for a contact
        result = address_book.search_contact("Alice")
        if result:
            print("Found contact:")
            for name, details in result.items():
                print(f"  Name: {name}")
                print(f"  Phone: {details['phone']}")
                print(f"  Email: {details['email']}")
                print(f"  Address: {details['address']}")
        else:
            print("Contact 'Alice' not found")
            
        # List all contacts
        print("\nAll contacts:")
        all_contacts = address_book.list_all_contacts()
        for name in all_contacts:
            print(f"  - {name}: {all_contacts[name]['phone']}")
            
        # Delete a contact
        address_book.delete_contact("Bob")
        print("\nAfter deleting Bob:")
        all_contacts = address_book.list_all_contacts()
        for name in all_contacts:
            print(f"  - {name}: {all_contacts[name]['phone']}")
            
        # Clean up
        os.remove(test_file)
        
    except Exception as e:
        print(f"Error in address book test: {e}")

if __name__ == "__main__":
    # Import csv here to avoid confusion with the globally imported modules
    import csv
    
    print("===== Medium Assignment Demonstration =====")
    
    test_fibonacci()
    test_word_frequency()
    test_data_validation()
    test_student_grades()
    test_address_book()
    
    print("\n===== All tests completed =====")
