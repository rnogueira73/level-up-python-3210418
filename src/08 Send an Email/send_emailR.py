import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(emailTo,emailSubjet,emailBody):
  port = 587
  emailFrom = "ruben_nogueira@hotmail.com"
  password = input("Type your password and press enter:")

  message = MIMEMultipart()
  message["From"] = emailFrom
  message["To"] = emailTo
  message["Subject"] = emailSubjet
  message.attach(MIMEText(emailBody, "plain"))
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.office365.com", port) as server:
     server.starttls()
     server.login(emailFrom,password)
     server.sendmail(emailFrom, emailTo, message)


if __name__ == '__main__':
    # replace receiver email address
    send_email('rubennogueiraromero@gmail.com', 'Notification', 'Everything is awesome!')
