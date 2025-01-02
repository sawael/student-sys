# Student Management System (SMS)

A Python-based platform that facilitates student and teacher management, along with course registration capabilities. The system is designed to be accessible on multiple platforms, including desktops, tablets, and smartphones.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [User Classes](#user-classes)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database Details](#database-details)
- [File Structure](#file-structure)
- [Technical Architecture](#technical-architecture)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Student Management System (SMS) is designed to streamline student enrollment and provide a centralized platform for academic management. It serves as a comprehensive solution for educational institutions to improve operational efficiency.

### Key Benefits
- Centralized student record management
- Efficient course registration system
- Streamlined communication between stakeholders
- Multi-platform accessibility

## Features

### Course Enrollment
- Search functionality for available courses
- Streamlined enrollment process
- Course schedule viewing

### Role-Based Access

#### Student Access
- View assigned courses
- Access teacher information
- Course details lookup

#### Teacher Access
- View assigned courses
- Student roster management
- Course management tools

#### Admin Access
- Complete user account management
  - Create, update, and delete accounts
  - Manage user roles
- Course administration
  - Schedule management
  - Teacher assignments
- System-wide oversight

## System Requirements

### Hardware Requirements

#### Minimum Specifications
- **Processor:** Dual-core 2.0 GHz or higher
- **RAM:** 4 GB minimum
- **Storage:** 2 GB free space
- **Display:** 1280x720 resolution or higher

### Software Requirements

#### Backend
- Python (version TBD)
- SQLite database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sawael/student_sys.git
cd student_sys
```

2. Run the application:
```bash
python student_management.py
```

## Usage

### Login Screen
- Upon running the program, the login screen appears
- Users can log in as an admin, teacher, or student

### Admin Panel
- Manage teachers and students
- Add, edit, or delete user records

### Teacher Panel
- Access student information
- Perform relevant CRUD operations on student data

### Student Panel
- View personal data and academic information

## Database Details

### Default Credentials

#### Admin Access
| Username | Password |
|----------|----------|
| admin    | admin    |

#### Teacher Access
| Name             | Username      | Password    |
|------------------|---------------|-------------|
| Dr Ahmed Atef    | ahmedatef     | 123atef    |
| Dr Ahmed Samir   | ahmedsamir    | 123samir   |
| Dr Sayed Shawkat | sayedshawkat  | 123shawkat |

#### Student Access
| Name  | Username | Password |
|-------|----------|----------|
| Ahmed | ahmed    | ahmed    |
| Alaa  | alaa     | alaa     |
| Nader | nader    | nader    |

### Course Information
| Course Name         | Teacher ID |
|--------------------|------------|
| Math 1             | 1          |
| Software Engineering| 2          |
| Machine Learning   | 3          |

## File Structure

```
smsFinal/
├── adminPanel.py        # Admin functionalities for managing data
├── teacherPanel.py      # Teacher functionalities for managing courses and grades
├── studentPanel.py      # Student functionalities for viewing courses and grades
├── database.py          # Handles database interactions
├── stdmng.py           # Manages student data
├── mainSMS.py          # Main script to run the application
├── sms.db              # SQLite database file
└── README.md           # Documentation
```

## Technical Architecture

### Database Schema
- The Database class initializes and manages the SQLite database
- Creates tables for admins, teachers, and students if they don't exist
- Handles all database interactions through structured queries

### File Descriptions
- **sms.db**: SQLite database containing all system data
- **mainSMS.py**: Main script to run the application
- **adminPanel.py**: Admin functionalities for managing data
- **teacherPanel.py**: Teacher functionalities for managing courses and grades
- **studentPanel.py**: Student functionalities for viewing courses and grades
- **database.py**: Handles database interactions
- **stdmng.py**: Manages student data

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open-source and available under the MIT License.
