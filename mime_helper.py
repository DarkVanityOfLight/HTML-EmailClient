from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_html_part(html):
    return MIMEText(html, "html")

def create_plain_part(text):
    return MIMEText(text, "plain")

def create_mixed_multipart(*args):
    return MIMEMultipart(_subparts=args)

def create_alternative_multipart(*args)
    return MIMEMultipart(_subparts=args, _subtype="alternative")

if __name__ == "__main__":

    from email.message import EmailMessage

    part1 = create_html_part("Foo")
    part2 = create_plain_part("Bar")
    multipart = create_mixed_multipart(part1, part2)
    msg = EmailMessage()
    msg.set_content(multipart)

    print(msg.as_string())
