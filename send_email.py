import smtplib
import os

def sendMessage(recipients, message):
  sender_email = os.getenv('EMAIL')
  email_password = os.getenv('PASS')
  auth = (sender_email, email_password)
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(auth[0], auth[1])
  server.sendmail(auth[0], recipients, message)

def main():
  recipients = os.getenv('RECIPIENTS').split(',')
  message = os.getenv('MESSAGE').replace("\\n","\n")
  sendMessage(recipients, message)

if __name__ == '__main__':
  main()
