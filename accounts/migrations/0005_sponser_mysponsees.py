# Generated by Django 3.0 on 2020-12-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201111_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponser',
            name='mysponsees',
            field=models.ManyToManyField(to='accounts.Sponsee'),
        ),
    ]
