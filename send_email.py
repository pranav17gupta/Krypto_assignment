import smtp

/*method to send email*/
@staticmethod
def sendEmail(userid, crypto, price):
  sender_email = "pranavtest123@rabbitmq.co.in"
  rec_email = email
  password = "test123";
  message = "Hii, " + userid + "\nAlert!! current price of " + crypto + " reaches to " + price
  
  server = smtp.SMTP(rabbitmq@SERVER-IP)
  server.starttls()
  server.login(sender_email, password)
  print("Login success")
  server.sendmail(sender_email, reciever_email, message)
  print("Email has sent to ", rec_email)

