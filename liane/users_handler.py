# liane/users_handler.py

import sqlite3
import os

def add_user(email, name=None):
    """
    Adds a new user to the 'users' table.
    """
    conn = sqlite3.connect('instance.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (email, name, is_active)
            VALUES (?, ?, 1)
        ''', (email, name))
        conn.commit()
        print(f"User {email} added.")
    except sqlite3.IntegrityError:
        print(f"User {email} already exists.")
    finally:
        conn.close()

def is_active_user(email):
    """
    Checks if the given email belongs to an active user.

    Args:
        email (str): The sender's email address.

    Returns:
        bool: True if the user is active, False otherwise.
    """
    if not email:
        return False

    db_path = os.path.abspath('instance.db')

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT is_active FROM users WHERE email = ?
            ''', (email.lower(),))
            result = cursor.fetchone()
            if result:
                return result[0] == 1  # 1 for active, 0 for inactive
            else:
                return False  # Email not found
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred while checking active user: {db_err}")
        return False
    except Exception as ex:
        print(f"An unexpected error occurred while checking active user: {ex}")
        return False

def deactivate_user(email):
    conn = sqlite3.connect('instance.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET is_active = 0 WHERE email = ?
    ''', (email.lower(),))
    conn.commit()
    conn.close()
    print(f"User {email} deactivated.")


def is_active_user(email):
    """
    Checks if the given email belongs to an active user.
    
    Args:
        email (str): The sender's email address.
    
    Returns:
        bool: True if the user is active, False otherwise.
    """
    if not email:
        return False

    db_path = os.path.abspath('instance.db')

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT is_active FROM users WHERE email = ?
            ''', (email.lower(),))
            result = cursor.fetchone()
            if result:
                return result[0] == 1  # 1 for active, 0 for inactive
            else:
                return False  # Email not found
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred while checking active user: {db_err}")
        return False
    except Exception as ex:
        print(f"An unexpected error occurred while checking active user: {ex}")
        return False
