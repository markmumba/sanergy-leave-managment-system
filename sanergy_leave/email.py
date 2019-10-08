from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def welcome_email(name,receiver, password):
    subject ='link to your to the lms'
    sender = 'sprovider549@gmail.com'

    text_content = render_to_string('email/welcome.txt',{"name": name, "password":password})
    html_content = render_to_string('email/welcome.html',{"name":name, "password":password})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


# status approval/declined emails

def status_approval_email(name,receiver,date,date2):
    subject= 'Leave has been accepted'
    sender ='sprovider549@gmail.com'

    text_content = render_to_string('email/accepted.txt',{"name":name,"date":date,"date2":date2})
    html_content = render_to_string('email/accepted.html',{"name":name,"date":date,"date2":date2})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def status_declined_email(name,receiver):
    subject='Leave application has been rejected'
    sender = 'sprovider549@gmail.com'

    text_content = render_to_string('email/declined.txt',{"name": name})
    html_content = render_to_string('email/declined.html')

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

