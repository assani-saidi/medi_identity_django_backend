# Generated by Django 4.0.4 on 2022-05-20 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_alter_patient_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='image',
        ),
    ]
