import sqlite3
import os

def add_answered_column_if_not_exists():
    """
    Adds a boolean 'answered' column to the 'emails' table if it doesn't already exist.
    The default value for the column is set to False (0).
    """
    # Connect to the SQLite database
    db_path = os.path.abspath('instance.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if 'answered' column exists in the 'emails' table
    cursor.execute("PRAGMA table_info(emails)")
    columns = [column_info[1] for column_info in cursor.fetchall()]
    if 'answered' not in columns:
        # Add the 'answered' column with default value False (0)
        cursor.execute("ALTER TABLE emails ADD COLUMN answered INTEGER DEFAULT 0")
        conn.commit()
        print("Added 'answered' column to 'emails' table.")
    else:
        print("'answered' column already exists in 'emails' table.")

    # Close the database connection
    conn.close()

def create_users_table():
    """
    Creates the 'users' table in the 'instance.db' database if it doesn't exist.
    """
    db_path = os.path.abspath('instance.db')
    conn = sqlite3.connect(db_path)
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
    conn.close()
    print("Users table is ready.")