Student Grades Management System

Project Overview
The Student Grades Management System is a modular Python-based Console application designed to help teachers and administrators manage student academic records efficiently.


Unlike a simple script, this project utilizes a modular architecture, splitting functionality into logical components to ensure code readability, maintainability, and scalability. It demonstrates core computer science concepts including CRUD operations (Create, Read, Update, Delete), dictionary manipulation, and robust exception handling.


Features
Add Student: Create new records with unique names and grades.

Update Records: Modify grades for existing students.

Delete Records: Remove students who have left or graduated.

View All: Display a formatted list of all students currently in the system.

Input Validation: Robust error handling ensures the program does not crash if the user enters invalid data (e.g., text instead of numbers).

Modular Design: Code is split into main.py (Interface), operations.py (Logic), and utils.py (Helpers).


Technologies & Tools Used
Language: Python 3.x

IDE/Editor: VS Code 

Concepts: Data Structures (Dictionaries), Modular Programming, Exception Handling (try-except).


 Project Structure
This project consists of three specific modules:

main.py: The entry point of the application. It handles the menu loop and user interface.

operations.py: Contains the backend logic for adding, updating, deleting, and fetching data.

utils.py: Contains utility functions for validating user inputs (ensuring grades are integers, names are not empty).

⚙️ How to Install & Run
Prerequisites: Ensure you have Python installed on your system. You can check this by typing python --version in your terminal.

Download the Project: Download the project folder or clone the repository.

Bash

git clone <repository_url>
Navigate to the Directory: Open your terminal or command prompt and change the directory to the project folder.

Bash

cd student-grades-system
Run the Application: Execute the main script to start the program.

Bash

python main.py

Instructions for Testing
To verify the system works as intended, follow these steps:

Test Adding: Select option 1. Enter a name (e.g., "Sagar") and a grade (e.g., "90").

Test Validation: Select option 1 again. Enter a name, but for the grade, type "abc". The system should catch the error and ask for a number again.

Test Updating: Select option 2. Enter "Sagar" and change the marks to "95".

Test Viewing: Select option 4. Verify that "Sagar" now has "95".

Test Deleting: Select option 3. Delete "Sagar" and use option 4 to confirm the list is empty.


Screenshots
(Note: Replace the text below with actual screenshots of your running code to impress the evaluator)

1. Main Menu & Adding a Student

2. Error Handling (Input Validation)
   

Future Improvements
File Handling: Save data to a .txt or .csv file so records persist after closing the program.

GUI: Create a graphical interface using Tkinter.

Student ID: Implement unique IDs to handle students with the same name.

