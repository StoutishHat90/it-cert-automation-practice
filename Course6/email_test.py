#imports
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

#defines the mail server using the local host
#mail_server = smtplib.SMTP_SSL('google.com')
mail_server = smtplib.SMTP('localhost')



# message = EmailMessage()
# print(message)

# sender = "stoutishhat90@gmail.com"
# recipient = "bdawespetrie@gmail.com"
# password = "password"

# message['From'] = sender
# message['To'] = recipient
# print(message)

# message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
# print(message)

# body = """Hey there!

# I'm learning to send emails using Python!"""
# message.set_content(body)