#.....STUDENT GRADE MANAGEMENT SYSTEM....

# operations.py
# This module handles all database operations for the student system.

# Using a dictionary to store data globally within this module
student_grades = {}

def add_student(name, grade):
    """Adds a new student to the dictionary."""
    if name in student_grades:
        print(f"Warning: {name} already exists! Use update to change marks.")
    else:
        student_grades[name] = grade
        print(f"--> Success: Added {name} with {grade} marks.")

def update_student(name, grade):
    """Updates the grade of an existing student."""
    if name in student_grades:
        student_grades[name] = grade
        print(f"--> Success: Updated {name}'s marks to {grade}.")
    else:
        print(f"--> Error: {name} was not found in the system.")

def delete_student(name):
    """Removes a student from the dictionary."""
    if name in student_grades:
        del student_grades[name]
        print(f"--> Success: {name} has been deleted.")
    else:
        print(f"--> Error: {name} was not found.")

def display_all_students():
    """Prints a list of all students and their grades."""
    print("\n--- Current Student List ---")
    if student_grades:
        for name, grade in student_grades.items():
            print(f"Student: {name} | Grade: {grade}")
    else:
        print("(No students found in the database)")
    print("----------------------------")