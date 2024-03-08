import psycopg2

# Function to establish a database connection
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname="A3",
            user="postgres",
            password="Andy19950729",
            host="localhost",
            port="5432"
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
        return None

# Function to close the database connection
def close_database_connection(connection):
    if connection:
        connection.close()

# Function to retrieve all students from the database
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(student)
    except psycopg2.Error as e:
        print("Error retrieving students:", e)

# Function to add a new student to the database
def add_student(connection, first_name, last_name, email, enrollment_date):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date)
        )
        connection.commit()
        print("Student added successfully.")
    except psycopg2.Error as e:
        print("Error adding student:", e)

# Function to update a student's email
def update_student_email(connection, student_id, new_email):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )
        connection.commit()
        print("Email updated successfully.")
    except psycopg2.Error as e:
        print("Error updating email:", e)

# Function to delete a student from the database
def delete_student(connection, student_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )
        connection.commit()
        print("Student deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting student:", e)

# Main function
def main():
    connection = connect_to_database()
    if not connection:
        return

    while True:
        print("\nOptions:")
        print("1. Retrieve all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_all_students(connection)
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            add_student(connection, first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            new_email = input("Enter new email: ")
            update_student_email(connection, student_id, new_email)
        elif choice == "4":
            student_id = input("Enter student ID: ")
            delete_student(connection, student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    close_database_connection(connection)

if __name__ == "__main__":
    main()
