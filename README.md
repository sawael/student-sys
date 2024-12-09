Student Management System

Description

This is a Student Management System (SMS) built using Python. It provides an interface to manage students, teachers, and administrators, enabling user authentication and database interactions. The system leverages SQLite as its database and Tkinter for the graphical user interface (GUI).

Features

	•	User Authentication: Admins, teachers, and students have separate login mechanisms.
	•	Database Setup: Automatically initializes a local SQLite database with required tables (admins, teachers, students).
	•	CRUD Operations: Add, view, edit, and delete student/teacher records.
	•	GUI: Simple and interactive user interface built using Tkinter.
	•	Data Persistence: Data is stored locally in an SQLite database (sms.db).

Getting Started

Prerequisites

Ensure you have the following installed:
	•	Python (Latest Version)
	•	Required Python libraries:
	•	sqlite3 
	•	tkinter 
 
pip install sqlite-utils
pip install tkinter

Installation

	1.	Clone the repository:

git clone https://github.com/sawael/student_sys.git
cd StudentManagementSystem

	2.	Run the application:

python student_management.py



Usage

	1.	Login Screen:
 
Upon running the program, the login screen appears. Users can log in as an admin, teacher, or student.
	2.	Admin Panel:
	  •	Manage teachers and students.
	  •	Add, edit, or delete user records.
	3.	Teacher Panel:
	  •	Access student information.
	  •	Perform relevant CRUD operations on student data.
	4.	Student Panel:
	  •	View personal data and academic information.

Database Details

	•	Database Name: sms.db
	•	admins: Stores administrator credentials.
	•	teachers: Stores teacher information and credentials.
	•	students: Stores student information and credentials.

File Structure

	•	student_management.py: Main application file containing GUI and database logic.
	•	sms.db: SQLite database file (auto-generated upon running the script).

Code Overview

Database Initialization

The Database class is responsible for initializing and managing the SQLite database. It creates tables for admins, teachers, and students if they do not exist.

GUI

Tkinter is used to build the user interface, with separate screens for login, admin, teacher, and student functionalities.

Key Classes

	•	Database: Handles database connections and queries.
	•	App: Manages the application GUI flow.

Contributing

	1.	Fork the repository.
	2.	Create a new branch for your feature/bugfix.
	3.	Commit your changes and push them to your branch.
	4.	Open a pull request for review.
