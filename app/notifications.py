import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT")  # This should be yourphonenumber@carrier_gateway.com

def send_sms_alert(body):
    """
    Send an SMS alert to the user via Email-to-SMS gateway.
    """
    msg = MIMEText(body)
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT
    msg["Subject"] = ""  # Subject not needed for SMS

    # Connect to Gmail SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT, msg.as_string())

    print("SMS sent via Email-to-SMS!")

# Test your SMS sending!
if __name__ == "__main__":
    send_sms_alert("🚗 Your Tesla is less than 5 minutes away from your location!")