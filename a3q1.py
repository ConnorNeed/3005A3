import psycopg2
import datetime

TABLENAME = "students"

connection = psycopg2.connect(database = "Assignment3", 
                              user = "postgres", 
                              host= 'localhost',
                              password = "1902",
                              port = 5432)
cur = connection.cursor()

def getAllStudents():
    #query for all items in the table
    cur.execute('SELECT * FROM '+TABLENAME+';')
    #get the output
    rows = cur.fetchall()
    #display the output in a table
    for row in rows:
        for cell in row:
            print(cell, end="\t")
        print()
    print()

def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute(f"""INSERT INTO {TABLENAME} (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);""",
                (TABLENAME, first_name, last_name, email, enrollment_date))
def updateStudentEmail(student_id, new_email):
    cur.execute(f"UPDATE {TABLENAME} SET email = '{new_email}' WHERE student_id = {student_id};")

def deleteStudent(student_id):
    cur.execute(f"DELETE FROM {TABLENAME} WHERE student_id={student_id};")

getAllStudents()
# addStudent("Connor", "Needham", "connor@email.com", datetime.date(2024, 3, 18))
getAllStudents()
updateStudentEmail(13, "jd@email.com")
getAllStudents()
deleteStudent(16)

# commit and close connection
connection.commit()
cur.close()
connection.close()