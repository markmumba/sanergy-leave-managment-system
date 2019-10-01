from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def acceptance_email(name,receiver):
    subject= 'Leave has been accepted'
    sender ='sprovider549@gmail.com'

    text _content = render_to_string('email/accepted.txt')
    html_content = render_to_string('email/accepted.html')

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])