# liane/main.py

import os
from dotenv import load_dotenv

# Step 1: Load the .env file from the root directory of the liane project, if needed.
# Adjust the path to point to the correct location of your .env file.
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
#print(f"Loading environment variables from: {dotenv_path}")
load_dotenv(dotenv_path)  # Load environment variables from `.env`, if it exists.

# Step 2: Verify that environment variables are correctly loaded (optional debug).
#print(f"Loaded EMAIL_USERNAME: {os.getenv('EMAIL_USERNAME')}")
#print(f"Loaded EMAIL_PASSWORD: {os.getenv('EMAIL_PASSWORD')}")
#print(f"Loaded IMAP_SERVER: {os.getenv('IMAP_SERVER')}")
#print(f"Loaded ORGANIZATION_ID: {os.getenv('ORGANIZATION_ID')}")
#print(f"Loaded OPENAI_PROJECT_ID: {os.getenv('OPENAI_PROJECT_ID')}")
#print(f"Loaded OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

# Step 3: Ensure that required environment variables are set before importing `ellis`.
if not os.getenv("EMAIL_USERNAME") or not os.getenv("EMAIL_PASSWORD") or not os.getenv("IMAP_SERVER"):
    raise EnvironmentError("EMAIL_USERNAME, EMAIL_PASSWORD, and IMAP_SERVER must be set in your environment.")

# Step 4: Import `ellis` after confirming environment variables are set.
from ellis import get_history, get_new_messages

# Step 5: Import `kate` after loading environment variables.
from kate import get_response

# Step 6: Example usage: Fetch email history using `ellis`.
new_messages = get_new_messages()
history = get_history("alex@ruco.pt")

print(f"history: {history}")

# Choose which AI model to use by uncommenting the appropriate line
ai = "gemma2:2b"  # Option 1: Treat 'gemma2:2b' as a distinct model.
# ai = "phi3"      # Option 2: Use 'phi3'.
# ai = "gpt3"      # Option 3: Use GPT-3.
# ai = "gpt4o"     # Option 4: Use GPT-4.
# ai = "gpt4-turbo" # Option 5: Use GPT-4 Turbo.

# Example prompt to send to the AI model.
#prompt = "What is the capital of France?"

# Step 7: Use `get_response` to send the prompt to the chosen AI model.
#response = get_response(prompt, ai)

# Step 8: Print the response from the AI model.
#print(f"AI Model Response: {response}")
