# Generated by Django 3.0 on 2020-11-11 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_sponser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reason',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Sponsee'),
        ),
        migrations.AlterField(
            model_name='school',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Sponsee'),
        ),
    ]
