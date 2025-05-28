import re

def validate_input(value, data_type):
    """
    Validates if the input value matches the specified data type.

    Args:
        value (str): The input value to validate.
        data_type (str): The expected data type ('integer', 'float', 'email', etc.).

    Returns:
        bool: True if the value is valid for the specified data type, False otherwise.
    """
    if data_type.lower() == "integer":
        try:
            int(value)
            return True
        except ValueError:
            return False
            
    elif data_type.lower() == "float":
        try:
            float(value)
            return True
        except ValueError:
            return False
            
    elif data_type.lower() == "email":
        # Basic email validation pattern
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_pattern, value):
            return True
        return False
        
    elif data_type.lower() == "date":
        # Basic date validation (format: YYYY-MM-DD)
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if re.match(date_pattern, value):
            try:
                year, month, day = map(int, value.split('-'))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return True
            except:
                pass
        return False
        
    elif data_type.lower() == "phone":
        # Basic phone number validation
        phone_pattern = r'^\+?[\d\s\-\(\)]{8,20}$'
        if re.match(phone_pattern, value):
            return True
        return False
        
    else:
        raise ValueError(f"Unsupported data type: {data_type}")
