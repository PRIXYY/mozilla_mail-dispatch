import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

def send_email(sender_email, sender_password, recipients, subject, body, smtp_server="smtp.gmail.com", smtp_port=587, batch_size=100):
    """
    Sends emails in batches of `batch_size` to avoid SMTP limits.

    Parameters:
    - sender_email (str): The sender's email address.
    - sender_password (str): The sender's email password or App Password.
    - recipients (list): List of email addresses (sent in BCC).
    - subject (str): Subject of the email.
    - body (str): Email content.
    - smtp_server (str, optional): SMTP server (default: Gmail).
    - smtp_port (int, optional): SMTP port (default: 587).
    - batch_size (int, optional): Max recipients per batch (default: 100).

    Returns:
    - None
    """
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Split recipients into batches
        for i in range(0, len(recipients), batch_size):
            batch = recipients[i:i + batch_size]  # Get next batch

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            server.sendmail(sender_email, batch, msg.as_string())  # Send to batch
            print(f"Sent batch {i // batch_size + 1}: {len(batch)} emails")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print("Error sending email:", e)


def addreceipients(start,end,recipients):
    url = "https://docs.google.com/spreadsheets/d/__KEY__/export?format=xlsx"
    df = pd.read_excel(url, engine="openpyxl")
    start_row = start;  
    end_row = end;    
    for i in range(start_row, min(end_row, len(df))):
        if(df.iloc[i,6]=="DONE" ):
            recipients.append(df.iloc[i,3])



# Example Usage
if __name__ == "__main__":
    sender_email = "YOUR_EMAIL"
    sender_password = "YOUR APP PASSWORD" 
    start = 0  # give start value here
    end = 100 # give end value here 
    recipients = []  
    addreceipients(start,end,recipients)
    subject = "Test Email"
    body = "Hello, this is a test email sent using Python SMTP with batching!"

    send_email(sender_email, sender_password, recipients, subject, body)
