from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def acceptance_email(name,receiver):
    subject= 'Leave has been accepted'
    sender ='sprovider549@gmail.com'

    text_content = render_to_string('email/accepted.txt')
    html_content = render_to_string('email/accepted.html')

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def declined_email(name,reciver):
    subject='Leave application has been rejected'
    sender = 'sprovider549@gmail.com'

    text_content = render_to_string('email/declined.txt')
    html_content = render_to_string('email/declined.html')

    msg = EmailMultiAlternatives(subject,text_content,sender,[reciever])