import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students
(
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    (101, "Kapil", 85)
)

connection.commit()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

for student in data:
    print(student)

connection.close()