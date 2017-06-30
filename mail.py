#senting emails with gmail servor

import smtplib
try:
  smtpobj=smtplib.SMTP_SSL('smtp.gmail.com',465)
  smtpobj.ehlo()
  #smtpobj.starttls()
except Exception as e:
    print('connection error '+ str(e))
try:
   smtpobj.login('shahules786@gmail.com',input('password:'))
   resp=input("enter recepient mail id")
   

   p=smtpobj.sendmail('shahules786@gmail.com',resp,'subject:ignore.\n hii,there.am using python.')
   print(p)
except Exception as e:
    print('error'+str(e))
