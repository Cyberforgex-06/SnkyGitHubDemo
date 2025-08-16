import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject, body, to_email):
    from_email = os.getenv('EM_USERNAME')
    password = os.getenv('EM_PASSWORD')

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = f"GitHub Actions <{from_email}>"
    msg['To'] = to_email

    # Connect to the SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Example email content
    subject = "New Commit and Snyk Scan Report"
    body = "A new commit was pushed and Snyk scan completed.\nCheck the GitHub Actions logs for details."
    to_email = "your.email@example.com"

    print("Running Python script...")
    send_email(subject, body, to_email)
