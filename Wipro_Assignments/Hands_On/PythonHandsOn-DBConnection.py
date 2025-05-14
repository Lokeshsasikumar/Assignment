import mysql.connector

# Exercise 1: Connecting to MySQL Database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='loky123',
            database='test_db'
        )
        print("Successfully connected to the database.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Exercise 2: Creating a Table
def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
    """)
    print("Table 'users' created successfully.")

# Exercise 3: Inserting Data into the Table
def insert_user(connection, name, email):
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    connection.commit()
    print(f"User {name} inserted successfully.")

# Exercise 4: Querying Data from the Table
def get_all_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# Exercise 5: Updating Data in the Table
def update_user_email(connection, user_id, new_email):
    cursor = connection.cursor()
    query = "UPDATE users SET email = %s WHERE id = %s"
    cursor.execute(query, (new_email, user_id))
    connection.commit()
    print(f"User with ID {user_id} updated successfully.")

# Exercise 6: Deleting Data from the Table
def delete_user(connection, user_id):
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print(f"User with ID {user_id} deleted successfully.")

# Exercise 7: Using Parameters in Queries
def get_user_by_id(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    if result:
        print(f"ID: {result[0]}, Name: {result[1]}, Email: {result[2]}")
    else:
        print(f"No user found with ID {user_id}.")

# Exercise 8: Using Transactions
def insert_multiple_users(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("START TRANSACTION;")
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Bob", "bob@example.com"))
        connection.commit()
        print("Multiple users inserted successfully.")
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Error: {err}. Transaction rolled back.")

# Exercise 9: Closing the Connection
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Database connection closed.")

# ---- Main Execution Flow ----
connection = connect_to_db()

if connection:
    create_users_table(connection)
    insert_user(connection, "John Doe", "john.doe@example.com")
    get_all_users(connection)
    update_user_email(connection, 1, "new.email@example.com")
    delete_user(connection, 2)
    get_user_by_id(connection, 1)
    insert_multiple_users(connection)
    close_connection(connection)
