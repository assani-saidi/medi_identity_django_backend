# Generated by Django 4.0.4 on 2022-05-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='dieses',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
