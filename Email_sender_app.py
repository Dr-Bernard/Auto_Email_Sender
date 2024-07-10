from email.message import EmailMessage
from app2 import EMAIL_PASSWORD
import ssl, smtplib


email_sender = 'benjulihotels@gmail.com'
email_password = EMAIL_PASSWORD

email_receiver = 'lesipog826@carspure.com'

subject = 'Thank you for getting in touch with us today.'
body = '''
Thank you for contacting BENJULI HOTEL today. It was a great pleasure doing business with you and we would love to see more of you in no distant time.'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string()) 


