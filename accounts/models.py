from django.db import models
from django.contrib.auth.models import User
import datetime
from django.shortcuts import reverse


class Sponsee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=512)
    phone = models.CharField(max_length=12)
    birth_certificate = models.FileField(upload_to="media/birth_certificate/")
    national_id = models.FileField(upload_to="media/national_id/")

    def __str__(self):
        return self.user.username


def academic_level_choices():
    return [(r, r) for r in range(1, 13)]


def year_choices():
    return [(r, r) for r in range(datetime.date.today().year+1, datetime.date.today().year+13)]


class School(models.Model):
    student = models.OneToOneField("Sponsee", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    address = models.TextField(max_length=512)
    academic_level = models.IntegerField(
        choices=academic_level_choices(),
        default='1'
    )
    expected_year_of_completion = models.IntegerField(
        choices=year_choices(), default=datetime.date.today().year+3)

    def __str__(self):
        return self.name


class Reason(models.Model):
    student = models.OneToOneField('Sponsee', on_delete=models.CASCADE)
    reason = models.TextField(max_length=2048, null=False)

    # def __str__(self):
    #     return str(self.student.username) + " " + self.reason
    def get_absolute_url(self):
        return "reasons/{id}".format(id=self.id)


class Sponser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mysponsees = models.ManyToManyField("Sponsee")

    def __str__(self):
        return self.user.username
