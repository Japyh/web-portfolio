import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465 # 587

    USER_NAME = "jameqrecounter@gmail.com"
    PASSWORD = os.getenv("PORTFOLİO_PASSWORD")

    RECEIVER = "jameqrecounter@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(USER_NAME, PASSWORD)
        server.sendmail(from_addr=USER_NAME, to_addrs=RECEIVER, msg=message)
