import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
def gonder():
        smtp_server = "smtp.mailersend.net"
        smtp_port = 587
        email_address = "MS_wb8TiS@trial-351ndgw085x4zqx8.mlsender.net"
        email_password = "pADvOKZq0tRSPPao"

        # E-posta bilgileri
        receiver_email = "233502076@ogr.altinbas.edu.tr"
        subject = "Altınbaş Üniversitesi"
        body = f"Sevgili öğrencimiz, doğrulama kodunuz: \nSaygılarımızla."

        # E-posta oluşturma
        message = MIMEMultipart()
        message["From"] = email_address
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_address, email_password)
                server.send_message(message)
                print("E-posta başarıyla gönderildi!")
        except Exception as e:
            print(f"E-posta gönderim hatası: {e}")

gonder()
