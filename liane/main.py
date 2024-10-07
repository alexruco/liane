# liane/main.py

import os
from env_loader import load_env  # Import the env_loader module first

# Load environment variables before any other imports
load_env()

from db_handler import add_answered_column_if_not_exists, create_users_table
from messages_handler import process_unanswered_emails
from ellis import get_new_messages
from kate import get_response  # Now imported after environment variables are loaded
from message_responder import answer_emails
from users_handler import add_user

def main():
    # Fetch new messages using `ellis`.
    new_messages = get_new_messages()

    # Ensure the database schema is up-to-date.
    add_answered_column_if_not_exists()
    create_users_table()
    add_user('alex@ruco.pt', 'Alex Ruco', is_active=True)
    # Retrieve emails to process.
    emails_to_process = process_unanswered_emails()

    # Iterate over each email and process it.
    for email_id, email_data in emails_to_process:
        try:
            # Process the email.
            answer_emails(email_data)
            # No need to mark as answered here since it's already handled in process_unanswered_emails()
        except Exception as e:
            print(f"Error processing Email ID {email_id}: {e}")
            # Optionally, implement retry logic, log the error to a file, or handle it as needed.

    # Optional: Handle AI responses
    # ai = "gemma2:2b"  # Option 1: Treat 'gemma2:2b' as a distinct model.
    # ai = "phi3"        # Option 2: Use 'phi3'.
    # ai = "gpt3"        # Option 3: Use GPT-3.
    # ai = "gpt4o"       # Option 4: Use GPT-4.
    # ai = "gpt4-turbo"  # Option 5: Use GPT-4 Turbo.

    # Example prompt to send to the AI model.
    # prompt = "What is the capital of France?"

    # Use `get_response` to send the prompt to the chosen AI model.
    # response = get_response(prompt, ai)

    # Print the response from the AI model.
    # print(f"AI Model Response: {response}")

if __name__ == "__main__":
    main()
