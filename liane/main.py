# liane/main.py

import os
from dotenv import load_dotenv
from db_handler import add_answered_column_if_not_exists, create_users_table
from messages_handler import process_unanswered_emails
from ellis import get_new_messages
#from kate import get_response
from message_responder import answer_emails  # Ensure this is correctly implemented

def main():
    # Adjust the path to point to the correct location of your .env file.
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
    # print(f"Loading environment variables from: {dotenv_path}")
    load_dotenv(dotenv_path)  # Load environment variables from `.env`, if it exists.

    # Ensure that required environment variables are set before importing `ellis`.
    if not os.getenv("EMAIL_USERNAME") or not os.getenv("EMAIL_PASSWORD") or not os.getenv("IMAP_SERVER"):
        raise EnvironmentError("EMAIL_USERNAME, EMAIL_PASSWORD, and IMAP_SERVER must be set in your environment.")

    # Fetch new messages using `ellis`.
    new_messages = get_new_messages()

    # Add 'answered' column and create 'users' table if they don't exist.
    add_answered_column_if_not_exists()
    create_users_table()

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
