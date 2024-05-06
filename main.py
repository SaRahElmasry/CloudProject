import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

# Connect to MySQL DB
host = 'sql-server'
user = 'root'
password = '3124166'
database = 'cloud_db'

# Function to retrieve student records
def get_student_records():
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = db.cursor()

        student_query = "SELECT * FROM STUDENT"
        cursor.execute(student_query)
        students = cursor.fetchall()

        cursor.close()
        db.close()
        return students
    except mysql.connector.Error as err:
        print("Error:", err)
        return []

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/students')
def student_records():
    students = get_student_records()  # Retrieve student records
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
