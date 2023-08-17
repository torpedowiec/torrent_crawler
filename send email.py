import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "smithensonjohnie@gmail.com"
recipients = ["torpedowiec@icloud.com"]
password = ""


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP('localhost', 1025) as smtp_server:
       # smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string()) 
    print("Message sent!")


send_email(subject, body, sender, recipients, password)