import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables for email credentials
load_dotenv()
my_email = os.getenv("MY_EMAIL")  # Your email address from environment
my_password = os.getenv("MY_PASSWORD")  # Your email password from environment

def send_mail(subject, day, open_price, high_price, low_price, close_price, author, title, content, url, url_image):

    # Create an email message object
    message = EmailMessage()
    message["From"] = my_email  # Sender's email address
    message["To"] = "Your Email"  # Receiver's email address
    message["Subject"] = subject  # Subject line of the email

    # Construct the email body with stock and news data
    body = f"""
Date: {day}\n
Open price: ${round(float(open_price), 2)}
High price: ${round(float(high_price), 2)}
Low price: ${round(float(low_price), 2)}
Close price: ${round(float(close_price), 2)}

The News of Today:
Title: {title}
Author: {author}
Content: {content}

Read more: {url}
Image URL: {url_image}
"""

    message.set_content(body)  # Add the body content to the email
    try:
        # Establish a connection to the Gmail SMTP server
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=my_password)  # Login with credentials
            connection.send_message(message)  # Send the email
            print("Email sent successfully!")  # Confirm successful email sending
    except Exception as e:
        # Print error message if email fails
        print(f"An error occurred: {e}")
