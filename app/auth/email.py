
from flask import current_app
import urllib
# from flask_mail import Message

# from app import mail

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *


def send_email(to, subject, content):
	# print(to, subject, current_app.config['MAIL_DEFAULT_SENDER'], current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
	# msg = Message(
	# 	subject,
	# 	recipients=[to],
	# 	html=template,
	# 	sender=current_app.config['MAIL_DEFAULT_SENDER']
	# )
	# mail.send(msg)
	print('sendgrid',to,  current_app.config['SENDGRID_API_KEY'])
	sg = sendgrid.SendGridAPIClient(apikey=current_app.config['SENDGRID_API_KEY'], raise_errors=True)
	from_email = Email("namwkim85@gmail.com")
	to_email = Email(to)
	content = Content("text/html", content)
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	return response
