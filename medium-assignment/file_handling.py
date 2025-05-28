import csv
import os
import json

def calculate_student_averages(csv_file_path):
    """
    Reads a CSV file containing student data and calculates average grades.
    
    Expected CSV format: StudentName,Grade1,Grade2,Grade3,...
    
    Args:
        csv_file_path (str): Path to the CSV file.
        
    Returns:
        dict: A dictionary with student names as keys and their average grades as values.
    """
    student_averages = {}
    
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header if present
            
            for row in reader:
                if len(row) < 2:  # Need at least a name and one grade
                    continue
                    
                student_name = row[0]
                # Convert all grades to float and calculate average
                try:
                    grades = [float(grade) for grade in row[1:] if grade.strip()]
                    if grades:  # Check if there are any valid grades
                        average = sum(grades) / len(grades)
                        student_averages[student_name] = round(average, 2)
                except ValueError:
                    # Skip rows with non-numeric grades
                    print(f"Warning: Non-numeric grades found for {student_name}")
        
        return student_averages
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return {}


class AddressBook:
    """
    A simple text-based address book to store and retrieve contact information.
    """
    
    def __init__(self, file_path="address_book.json"):
        """
        Initialize an address book with the given file path.
        
        Args:
            file_path (str): Path to the JSON file for storing contacts.
        """
        self.file_path = file_path
        self.contacts = self._load_contacts()
    
    def _load_contacts(self):
        """
        Load contacts from the JSON file if it exists.
        
        Returns:
            dict: A dictionary of contacts.
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Warning: Address book file is corrupted. Creating a new one.")
                return {}
            except Exception as e:
                print(f"Error loading address book: {e}")
                return {}
        return {}
    
    def _save_contacts(self):
        """
        Save contacts to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.contacts, file, indent=4)
        except Exception as e:
            print(f"Error saving address book: {e}")
    
    def add_contact(self, name, phone, email="", address=""):
        """
        Add or update a contact in the address book.
        
        Args:
            name (str): Contact name.
            phone (str): Contact phone number.
            email (str, optional): Contact email.
            address (str, optional): Contact address.
            
        Returns:
            bool: True if contact was added/updated successfully.
        """
        if not name or not phone:
            print("Error: Contact name and phone number are required.")
            return False
            
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        
        self._save_contacts()
        return True
    
    def search_contact(self, name):
        """
        Search for a contact by name.
        
        Args:
            name (str): Name to search for.
            
        Returns:
            dict: Contact information or None if not found.
        """
        if name in self.contacts:
            return {name: self.contacts[name]}
        
        # Look for partial matches
        matches = {}
        for contact_name, details in self.contacts.items():
            if name.lower() in contact_name.lower():
                matches[contact_name] = details
                
        return matches if matches else None
    
    def delete_contact(self, name):
        """
        Delete a contact by name.
        
        Args:
            name (str): Name of the contact to delete.
            
        Returns:
            bool: True if contact was deleted successfully.
        """
        if name in self.contacts:
            del self.contacts[name]
            self._save_contacts()
            return True
        return False
    
    def list_all_contacts(self):
        """
        List all contacts in the address book.
        
        Returns:
            dict: All contacts in the address book.
        """
        return self.contacts
