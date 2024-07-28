import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="Ao5275/200018"   
        )

        if conn.is_connected():
            print("Connected to MySQL server")
            cursor = conn.cursor()
            create_database(cursor)
        else:
            print("Failed to connect to MySQL server")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Close the connection
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    main()
