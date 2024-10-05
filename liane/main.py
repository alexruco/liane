# liane/main.py

from dotenv import load_dotenv
import os
from env_loader import load_env, get_env_variable

# Step 1: Load the .env file from the root directory of the liane project
# Adjust the path to point to the correct location of your .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

dotenv_path_str = os.path.dirname(__file__)
print(f"dotenv_path:{dotenv_path}")

load_dotenv(dotenv_path)

# Step 2: Print to debug environment variables (optio
# nal)
print(f"Loaded ORGANIZATION_ID: {os.getenv('ORGANIZATION_ID')}")
print(f"Loaded OPENAI_PROJECT_ID: {os.getenv('OPENAI_PROJECT_ID')}")
print(f"Loaded OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

# Step 3: Import kate after loading environment variables
from kate import get_response

# Example prompt and AI model configuration
prompt = "What is the capital of France?"

# Choose which AI model to use by uncommenting the appropriate line
# ai = "gemma2:2b"  # Option 1: Treat 'gemma2:2b' as a distinct model
# ai = "phi3"      # Option 2: Use 'phi3'
ai = "gpt3"        # Option 3: Use GPT-3
# ai = "gpt4o"     # Option 4: Use GPT-4
# ai = "gpt4-turbo" # Option 5: Use GPT-4 Turbo

# Step 4: Use get_response to send the prompt to the chosen AI model
response = get_response(prompt, ai)

# Step 5: Print the response from the AI model
print(response)
