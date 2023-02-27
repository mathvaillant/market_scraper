import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

class Email:
  def __init__(self, **kwargs):
    self.sender = kwargs.pop('sender', None)
    self.sender_password = kwargs.pop('sender_password', None)
    self.receiver = kwargs.pop('receiver', None)
    self.email_content = kwargs.pop('email_content', None)
    self.subject = kwargs.pop('subject', None) 
    self.smtp_lib_config = kwargs.pop('smtp_lib_config', None)

  def build_email(self):
    email = MIMEMultipart()
    email['From'] = self.sender
    email['To'] = self.receiver
    email['Subject'] = self.subject

    body = self.email_content
    email.attach(MIMEText(body, 'plain'))
    self.email_content = email.as_string()

  def send_email(self):
    
    connection = smtplib.SMTP(self.smtp_lib_config)
    connection.starttls()

    connection.login(
      user=self.sender, 
      password=self.sender_password
    )

    connection.sendmail(
      from_addr=self.sender, 
      to_addrs=self.receiver, 
      msg=self.email_content
    )

    connection.close()


if __name__ == '__main__':
  try:
    with open("email.txt", "r") as file:
      email_content = file.read()

      sender = os.environ.get("MAIL_SENDER", "")
      sender_password = os.environ.get("MAIL_SENDER_PASSWORD", "")
      receiver = os.environ.get("MAIL_RECEIVER", "")
      smtp_lib_config = os.environ.get("SMTP_LIB_CONFIG", "")

      email = Email(
        sender=sender,
        sender_password=sender_password,
        receiver=receiver,
        email_content=email_content,
        smtp_lib_config=smtp_lib_config,
        subject="DAILY SUPERMARKET LIST 🥦🍌🍚"
      )

      email.build_email()
      email.send_email()
  except Exception as error:
    print("❌ Could not send the email: ", error)
  else:
    print("✅ 📤 Mail successfully sent!")

    
  



