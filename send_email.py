import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "abdulganiyu9023@gmail.com"
password="pgno dkrh usyp rjyo"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context) as server:
    server.login(username, password)

