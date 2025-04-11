# Student Result Management System

import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            subject TEXT,
            marks INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert(roll, name, subject, marks):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (?, ?, ?, ?)", (roll, name, subject, marks))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(roll):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE roll=?", (roll,))
    row = cur.fetchone()
    conn.close()
    return row

def update(roll, name, subject, marks):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=?, subject=?, marks=? WHERE roll=?", (name, subject, marks, roll))
    conn.commit()
    conn.close()

def delete(roll):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE roll=?", (roll,))
    conn.commit()
    conn.close()

connect()

while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by Roll Number")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == '1':
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        subject = input("Enter Subject: ")
        marks = int(input("Enter Marks: "))
        insert(roll, name, subject, marks)
        print("✅ Student added successfully.")

    elif choice == '2':
        students = view()
        for s in students:
            print(s)

    elif choice == '3':
        roll = int(input("Enter Roll No to search: "))
        student = search(roll)
        if student:
            print("🔍 Found:", student)
        else:
            print("❌ No record found.")

    elif choice == '4':
        roll = int(input("Enter Roll No to update: "))
        name = input("Enter New Name: ")
        subject = input("Enter New Subject: ")
        marks = int(input("Enter New Marks: "))
        update(roll, name, subject, marks)
        print("✏️ Student updated successfully.")

    elif choice == '5':
        roll = int(input("Enter Roll No to delete: "))
        delete(roll)
        print("🗑️ Student deleted successfully.")

    elif choice == '6':
        print("👋 Exiting...")
        break

    else:
        print("⚠️ Invalid choice! Try again.")
