import smtplib, ssl
from email.message import EmailMessage

port = 465



def send(sender_email, password, receiver_email, server, message):
    context = ssl.create_default_context()

    if isinstance(message, EmailMessage):
        message = message.as_string()

    with smtplib.SMTP_SSL(server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


