# utils.py
# This module handles input validation to prevent the program from crashing.

def get_valid_integer(prompt):
    """
    Repeatedly asks the user for input until they type a valid integer.
    This prevents the program from crashing if someone types 'abc' instead of a number.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number (e.g., 90, 1, 5).")

def get_valid_name(prompt):
    """Ensures the user doesn't leave the name blank."""
    while True:
        name = input(prompt).strip() # .strip() removes accidental spaces
        if len(name) > 0:
            return name
        else:
            print("Name cannot be empty. Please try again.")