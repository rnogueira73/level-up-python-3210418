import smtplib

def send_email(emailTo,emailSubjet,emailBody):
  port = 587
  emailFrom = "rubendeveloper73@gmail.com"
  password = input("Type your password and press enter:")
  message = f'Subject: {emailSubjet}\n\n{emailBody}'

  with smtplib.SMTP("smtp.gmail.com", port) as server:
     server.starttls()
     server.ehlo()
     server.login(emailFrom, password)
     server.sendmail(emailFrom, emailTo, message)


if __name__ == '__main__':
    # replace receiver email address
    send_email('rubennogueiraromero@gmail.com', 'Notification', 'Everything is awesome!')
