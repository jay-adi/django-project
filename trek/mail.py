import smtplib

def maiil(aaa):
  s = smtplib.SMTP('smtp.gmail.com', 587)


  s.starttls()


  s.login("email", "password")


  message = aaa

# sending the mail
  s.sendmail("email", "sender", message)

# terminating the session
  s.quit()
