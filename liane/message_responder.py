# liane/message_responder.py

from kate import get_response  # Import kate's get_response function
from ellis import send_message

def answer_emails(email_data):
    """
    Processes the email data by generating an AI-driven response and sending it back to the sender.
    
    Args:
        email_data (dict): Dictionary containing email details.
    """
    try:
        # Extract necessary details from email_data
        sender_email = email_data['sender']
        recipient_email = email_data['recipient']
        subject = email_data['subject']
        body = email_data['body']
        email_id = email_data['id']

        print(f"Answering Email ID {email_id} from {sender_email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")

        # Generate a prompt based on the email subject and body
        prompt = f"Subject: {subject}\n\nBody: {body}\n\nGenerate a professional and concise response to the above email."
        #prompt = "What is the capital of Brazil"
        # Use kate to generate a response
        ai_response = get_response(prompt, 'gemma2:2b')

        print(f"AI Response: {ai_response}")

        # Send the AI-generated response back to the sender
        send_message(subject, body, sender_email, recipient_email)

        print(f"Response sent to {sender_email} for Email ID {email_id}.")

    except Exception as e:
        print(f"Error in answer_emails for Email ID {email_id}: {e}")
        raise  # Re-raise the exception to be handled in the caller

