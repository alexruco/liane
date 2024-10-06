# liane/main.py

import os
from dotenv import load_dotenv
from db_handler import add_answered_column_if_not_exists, create_users_table
from messages_handler import process_unanswered_emails

# Adjust the path to point to the correct location of your .env file.
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
# print(f"Loading environment variables from: {dotenv_path}")
load_dotenv(dotenv_path)  # Load environment variables from `.env`, if it exists.

# Ensure that required environment variables are set before importing `ellis`.
if not os.getenv("EMAIL_USERNAME") or not os.getenv("EMAIL_PASSWORD") or not os.getenv("IMAP_SERVER"):
    raise EnvironmentError("EMAIL_USERNAME, EMAIL_PASSWORD, and IMAP_SERVER must be set in your environment.")

# Import `ellis` after confirming environment variables are set.
from ellis import get_history, get_new_messages

# Import `kate` after loading environment variables.
from kate import get_response

# Example usage: Fetch new messages using `ellis`.
get_new_messages()

# Add answered column and create users table
add_answered_column_if_not_exists()
create_users_table()

# Process unanswered emails
process_unanswered_emails()

# Optionally, handle AI responses
# ai = "gemma2:2b"  # Option 1: Treat 'gemma2:2b' as a distinct model.
# ai = "phi3"      # Option 2: Use 'phi3'.
# ai = "gpt3"      # Option 3: Use GPT-3.
# ai = "gpt4o"     # Option 4: Use GPT-4.
# ai = "gpt4-turbo" # Option 5: Use GPT-4 Turbo.

# Example prompt to send to the AI model.
# prompt = "What is the capital of France?"

# Use `get_response` to send the prompt to the chosen AI model.
# response = get_response(prompt, ai)

# Print the response from the AI model.
# print(f"AI Model Response: {response}")
