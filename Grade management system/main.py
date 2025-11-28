# main.py
# This is the main interface of the Student Grades Management System.

# Importing our custom modules
import operations
import utils 

def main():
    while True:
        print("**** STUDENT GRADES MANAGEMENT SYSTEM ****")
        print("1. Add a Student")
        print("2. Update a Student")  
        print("3. Delete a Student")  
        print("4. View All Students")  
        print("5. Exit")  

        # Using our utils module to safely get the menu choice
        choice = utils.get_valid_integer("Enter your choice (1-5): ")

        if choice == 1:
            name = utils.get_valid_name("Enter student name: ")
            grade = utils.get_valid_integer("Enter student grade: ")
            operations.add_student(name, grade)

        elif choice == 2:
            name = utils.get_valid_name("Enter student name to update: ")
            grade = utils.get_valid_integer("Enter new grade: ")
            operations.update_student(name, grade)
        
        elif choice == 3:
            name = utils.get_valid_name("Enter student name to delete: ")
            operations.delete_student(name)

        elif choice == 4:
            operations.display_all_students()

        elif choice == 5:
            print("Saving data... (simulation)")
            print("Closing the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 5.")   

# Standard boilerplate to run the main function
if __name__ == "__main__":
    main()