from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_staff_email(sponsor, sponsee):

    email_subject = 'Sponsor decided to sponsor a sponsee'
    email_body = 'Sponsor {sponsor} wants to sponsee {sponsee} with {email}.'.format(
        sponsor=sponsor.user.username, sponsee=sponsee.user.first_name, email=sponsee.user.email)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL, ],
    )
    return email.send(fail_silently=False)
