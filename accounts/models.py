from django.db import models
from django.contrib.auth.models import User


def academic_level_choices():
    return [(r, r) for r in range(1, 13)]


def year_choices():
    return [(r, r) for r in range(datetime.date.today().year+1, datetime.date.today().year+13)]


class Sponsee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=512)
    phone = models.CASCADE(max_length=12)
    birth_certificate = models.FileField(upload_to="birth_certificate/")
    national_id = models.FileField(upload_to="national_id/")

    def clean(self):
        try:
            phonenumbers.parse(self.phone, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError(
                _("Invalid phone number")
            )

    def __str__(self):
        return self.user.username
