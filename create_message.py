from email.message import EmailMessage


def create_new_message():
    return EmailMessage

def set_plain_text(msg, plain_text):
    msg.set_content(plain_text)

def set_html_alt(msg_part, html):
    msg_part.add_alternative(html, subtype="html")
