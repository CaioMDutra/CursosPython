import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


mail = "emaildocursorobos@gmail.com"
sendTo = "caimcd.dutra@hotmail.com, kyllerbhee@gmail.com, emaildocursorobos@gmail.com"

msg = MIMEMultipart()

msg["From"] = mail
msg["To"] = sendTo

msg["Subject"] = "Email de teste"
body = """Essa é um teste de envio de email"""

msg.attach(MIMEText(body, 'plain'))

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(mail, 'xrplwyivesgmvaej')

text = msg.as_string

s.sendmail(mail, sendTo, text)

s.quit()

