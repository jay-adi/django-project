import smtplib

def maiil(aaa):
  s = smtplib.SMTP('smtp.gmail.com', 587)


  s.starttls()


  s.login("vipul98saklani@gmail.com", "@UK07ax0643")


  message = aaa

# sending the mail
  s.sendmail("vipul98saklani@gmail.com", "vipul.cse17@nituk.ac.in", message)

# terminating the session
  s.quit()