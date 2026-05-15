# Student Management System

A simple Python-based Student Management System project developed using Python and MySQL. This project helps manage student records such as adding, viewing, updating, and deleting student details.

## Features

* Add new student records
* View all student details
* Update student information
* Delete student records
* MySQL database connectivity
* Simple and beginner-friendly project structure

## Technologies Used

* Python
* MySQL
* mysql-connector-python
* PyCharm

## Project Structure

```text
student_management_system/
│
├── Main.py
├── output.png
├── README.md
└── .venv/
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shaikfayazcareerprojects/student-management-system.git
```

### 2. Navigate to Project Folder

```bash
cd student-management-system
```

### 3. Install Required Package

```bash
pip install mysql-connector-python
```

## MySQL Database Setup

Create a database in MySQL:

```sql
CREATE DATABASE student_db;
```

Use the database:

```sql
USE student_db;
```

Create table:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
```

## Run the Project

```bash
python Main.py
```

## Output

The project successfully performs student management operations using Python and MySQL.

## GitHub Repository

Repository Link:

[https://github.com/shaikfayazcareerprojects/student-management-system](https://github.com/shaikfayazcareerprojects/student-management-system)

## Author

Shaik Fayaz

## Future Improvements

* Add GUI using Tkinter
* Add Login Authentication
* Export Student Data
* Search Functionality
* Web-based version using Flask or Django

## License

This project is created for educational and learning purposes.
