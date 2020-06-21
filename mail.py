#!/bin/bash/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''
Testing Failed.
'''
#the mail address and password
sender_address ='aayushpatel8122@gmail.com'
sender_pass ='Manhar4510'
receiver_address ='aayushpatel8122@gmail.com'
#setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Testing status'
#body and attachment
message.attach(MIMETextt(mail_content.'plain'))
#smtp session to send the mail
session = smtp.SMTP('smtp.gmail.com',587)#use gmail with port
session.starttls()#enable security
session.login(sender_address, sender_pass)#login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail sent')
