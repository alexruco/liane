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
    """
    conn = sqlite3.connect('instance.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT is_active FROM users WHERE email = ?
    ''', (email.lower(),))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0] == 1
    else:
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

def activate_user(email):
    conn = sqlite3.connect('instance.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET is_active = 1 WHERE email = ?
    ''', (email.lower(),))
    conn.commit()
    conn.close()
    print(f"User {email} activated.")
