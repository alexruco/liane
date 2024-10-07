# messages_handler.py

import sqlite3
import os
from users_handler import is_active_user
from ellis.utils import extract_email_address  # Ensure this is correctly implemented

def mark_email_as_answered(email_id):
    """
    Marks the specified email as answered in the 'emails' table.

    Args:
        email_id (int): The ID of the email to mark as answered.
    """
    db_path = os.path.abspath('instance.db')
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE emails
                SET answered = 1
                WHERE id = ?
            ''', (email_id,))
            conn.commit()
            print(f"Email ID {email_id} marked as answered.")
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred while marking Email ID {email_id} as answered: {db_err}")
    except Exception as ex:
        print(f"An unexpected error occurred while marking Email ID {email_id} as answered: {ex}")

def process_unanswered_emails(batch_size=10):
    """
    Retrieves unanswered emails from the database, checks if the sender is an active user,
    marks each email as answered, and returns a list of email_data to process.

    Args:
        batch_size (int): Number of emails to fetch per batch.

    Returns:
        list of tuples: Each tuple contains (email_id, email_data dict) for active users.
    """
    print("Starting to retrieve unanswered emails...")

    db_path = os.path.abspath('instance.db')
    emails_to_process = []

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            while True:
                # Retrieve a batch of unanswered emails
                cursor.execute('''
                    SELECT id, sender, recipient, subject, body
                    FROM emails
                    WHERE answered = 0
                    ORDER BY id ASC
                    LIMIT ?
                ''', (batch_size,))
                emails = cursor.fetchall()

                if not emails:
                    print("No more unanswered emails to retrieve.")
                    break  # Exit the loop if there are no more emails

                for email in emails:
                    email_id = email[0]
                    sender_full = email[1]
                    recipient_email = email[2]
                    subject = email[3]
                    body = email[4]

                    print(f"Evaluating Email ID {email_id} from '{sender_full}': '{subject}'")

                    # Extract the actual email address from the sender field
                    sender_email = extract_email_address(sender_full)
                    if not sender_email:
                        print(f"Failed to extract email address from '{sender_full}'. Skipping Email ID {email_id}.")
                        # Mark as answered to prevent infinite loops
                        mark_email_as_answered(email_id)
                        continue  # Skip processing if email extraction fails

                    # Check if the sender is an active user
                    if is_active_user(sender_email):
                        print(f"Sender '{sender_email}' is an active user. Preparing to process Email ID {email_id}.")
                        email_data = {
                            "id": email_id,
                            "sender": sender_email,
                            "recipient": recipient_email,
                            "subject": subject,
                            "body": body,
                        }
                        emails_to_process.append((email_id, email_data))
                    else:
                        print(f"Sender '{sender_email}' is NOT an active user. Skipping Email ID {email_id}.")

                    # Mark as answered regardless of active or not to prevent infinite loops
                    mark_email_as_answered(email_id)

    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred while retrieving unanswered emails: {db_err}")
    except Exception as ex:
        print(f"An unexpected error occurred while retrieving unanswered emails: {ex}")

    print(f"Retrieved {len(emails_to_process)} emails to process.")
    return emails_to_process
