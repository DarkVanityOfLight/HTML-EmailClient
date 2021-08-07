import smtplib, ssl
from email.message import EmailMessage


def get_default_port():
    return 465

def send(sender_email, password, receiver_email, server, message):
    context = ssl.create_default_context()

    if isinstance(message, EmailMessage):
        message = message.as_string()

    with smtplib.SMTP_SSL(server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def create_server(address):
    server = smtplib.SMTP(address)
    return server

def login_to_smtp(server, email, password):
    context = ssl.create_default_context()

    server.starttls()

    server.login(email, password)

def send_message_to_smtp(server, message):
    server.send_message(message)
