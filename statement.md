Project Statement: Student Grades Management System

1. 🚩 Problem Statement
In many educational institutions, the management of student academic records is still conducted using manual methods such as physical logbooks or unorganized spreadsheets. These traditional methods present several challenges:

Data Redundancy & Inconsistency: Manual entries often lead to duplicate records or mismatched data.

Inefficiency: Searching for a specific student's record in a physical pile or a massive spreadsheet is time-consuming.

Risk of Data Loss: Physical records can be damaged or lost, and simple files lack structure.

Lack of Validation: There are no automatic checks to prevent entering invalid grades (e.g., negative numbers or text).

There is a need for a digitized, structured, and automated system that allows faculty to perform operations on student data efficiently, ensuring data integrity and ease of access.


2. 🔭 Scope of the Project
The scope of the Student Grades Management System is defined as follows:

Core Functionality: The system will provide a Command Line Interface (CLI) to perform CRUD (Create, Read, Update, Delete) operations on student records.

Data Storage: The system uses ephemeral storage (Python Dictionaries) during runtime to demonstrate data structure manipulation.

Architecture: The project strictly follows a Modular Architecture, separating the user interface (main.py), business logic (operations.py), and helper functions (utils.py).

Error Handling: The scope includes robust exception handling to manage invalid user inputs without system failure.

Limitations: This version is a console-based application designed for a single user (local machine) and does not currently utilize an external database (SQL) or a Graphical User Interface(GUI).


3. 👥 Target Users
The primary users of this application are academic personnel who require a streamlined method for grading:

Class Teachers & Professors: For maintaining daily records of student performance.

Lab Assistants: For quickly logging practical marks during sessions.

School Administrators: For verifying student records and managing class lists.


4. 🌟 High-Level Features
The system is designed with the following key capabilities:

Student Registration: Allows the user to add new students with unique identifiers (names) and associated academic scores.

Dynamic Updates: Enables the modification of existing records to reflect re-evaluations or corrections in grades.

Record Removal: Provides functionality to delete obsolete or incorrect records from the system securely.

Global View: Offers a "Display All" feature to view the entire class list in a formatted, readable structure.

Input Sanitation: automatically detects non-integer inputs for grades or empty strings for names, preventing system crashes and ensuring data quality.


