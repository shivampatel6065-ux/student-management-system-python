import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",   # type your password here
    database="student_db"
)

cursor = connection.cursor()

# Add student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (%s, %s)",
        (name, age)
    )
    connection.commit()
    print("Student added successfully")

# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

# Update student
def update_student():
    stu_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))

    cursor.execute(
        "UPDATE students SET name=%s, age=%s WHERE id=%s",
        (name, age, stu_id)
    )
    connection.commit()
    print("Student updated successfully")

# Delete student
def delete_student():
    stu_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=%s"), (stu_id)
    connection.commit()
    print("Student deleted successfully")

# Menu
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program closed")
        break
    else:
        print("Invalid choice")

cursor.close()
connection.close()
