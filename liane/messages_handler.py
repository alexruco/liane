# messages_handler.py

import sqlite3
import os
from users_handler import is_active_user
from message_responder import answer_emails  # Ensure answer_emails is imported correctly

def process_unanswered_emails(batch_size=10):
    """
    Processes unanswered emails from the database in batches.
    For each unanswered email, checks if the sender is an active user.
    If so, sends the email data to answer_emails and marks the email as answered.
    """
    print("Starting to process unanswered emails...")

    # Define the path to the database
    db_path = os.path.abspath('instance.db')

    try:
        # Connect to the SQLite database using a context manager for safety
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
                    print("No more unanswered emails to process.")
                    break  # Exit the loop if there are no more emails

                for email in emails:
                    email_id = email[0]
                    sender_email = email[1]
                    recipient_email = email[2]
                    subject = email[3]
                    body = email[4]

                    print(f"Processing Email ID {email_id} from {sender_email}: '{subject}'")

                    # Check if the sender is an active user
                    if is_active_user(sender_email):
                        print(f"Sender {sender_email} is an active user.")
                        email_data = {
                            "id": email_id,
                            "sender": sender_email,
                            "recipient": recipient_email,
                            "subject": subject,
                            "body": body,
                        }

                        try:
                            # Send the email data to answer_emails
                            answer_emails(email_data)

                            # Mark the email as answered
                            cursor.execute('''
                                UPDATE emails
                                SET answered = 1
                                WHERE id = ?
                            ''', (email_id,))
                            conn.commit()
                            print(f"Email ID {email_id} processed and marked as answered.")
                        except Exception as e:
                            print(f"Error processing Email ID {email_id}: {e}")
                            # Optionally, implement retry logic or log the error for manual intervention
                    else:
                        print(f"Sender {sender_email} is not an active user. Skipping Email ID {email_id}.")
                        # Optionally, mark as answered to avoid reprocessing or handle accordingly
                        # Uncomment the following lines if you want to mark as answered even if inactive
                        cursor.execute('''
                             UPDATE emails
                             SET answered = 1
                             WHERE id = ?
                         ''', (email_id,))
                    conn.commit()
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred: {db_err}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

    print("Finished processing unanswered emails.")

