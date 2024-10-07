# db_handler.py

import sqlite3
import os

def add_answered_column_if_not_exists():
    """
    Adds a boolean 'answered' column to the 'emails' table if it doesn't already exist.
    The default value for the column is set to False (0).
    """
    db_path = os.path.abspath('instance.db')
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            # Check if 'answered' column exists
            cursor.execute("PRAGMA table_info(emails)")
            columns = [column_info[1] for column_info in cursor.fetchall()]
            if 'answered' not in columns:
                cursor.execute("ALTER TABLE emails ADD COLUMN answered INTEGER DEFAULT 0")
                conn.commit()
                print("Added 'answered' column to 'emails' table.")
            else:
                print("'answered' column already exists in 'emails' table.")
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred while adding 'answered' column: {db_err}")
    except Exception as ex:
        print(f"An unexpected error occurred while adding 'answered' column: {ex}")

def create_users_table():
    """
    Creates the 'users' table in the 'instance.db' database if it doesn't exist.
    """
    db_path = os.path.abspath('instance.db')
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            # Create the 'users' table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    name TEXT,
                    is_active INTEGER DEFAULT 1
                )
            ''')
            conn.commit()
            print("Users table is ready.")
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred while creating 'users' table: {db_err}")
    except Exception as ex:
        print(f"An unexpected error occurred while creating 'users' table: {ex}")
