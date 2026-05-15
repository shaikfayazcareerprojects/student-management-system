import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Techno@799",
    database="student_db"
)

cursor = conn.cursor()

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    sql = "INSERT INTO students(name, age, course) VALUES(%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(sql, values)
    conn.commit()

    print("Student Added Successfully")

# View Students
def view_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n--- Student List ---")

    for student in students:
        print(student)

# Search Student
def search_student():
    student_id = int(input("Enter Student ID: "))

    sql = "SELECT * FROM students WHERE id=%s"

    cursor.execute(sql, (student_id,))

    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print("Student Not Found")

# Update Student
def update_student():
    student_id = int(input("Enter Student ID: "))
    new_course = input("Enter New Course: ")

    sql = "UPDATE students SET course=%s WHERE id=%s"

    cursor.execute(sql, (new_course, student_id))

    conn.commit()

    print("Student Updated Successfully")

# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID: "))

    sql = "DELETE FROM students WHERE id=%s"

    cursor.execute(sql, (student_id,))

    conn.commit()

    print("Student Deleted Successfully")

# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")