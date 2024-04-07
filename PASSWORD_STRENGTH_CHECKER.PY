import re

def check_password_strength(password):
    # Define regex patterns for different character types
    has_uppercase = re.compile(r'[A-Z]')
    has_lowercase = re.compile(r'[a-z]')
    has_digit = re.compile(r'[0-9]')
    has_special = re.compile(r'[!@#$%^&*()_+=\[{\]};:<>|./?,-]')

    # Length check
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Complexity checks
    complexity = 0
    if has_uppercase.search(password):
        complexity += 1
    if has_lowercase.search(password):
        complexity += 1
    if has_digit.search(password):
        complexity += 1
    if has_special.search(password):
        complexity += 1
    
    # Determine strength based on complexity
    if complexity < 3:
        return "Moderate: Password should contain at least 3 of the following: uppercase letter, lowercase letter, digit, special character."
    else:
        return "Strong: Password meets the complexity requirements."

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
