# Generated by Django 3.1.3 on 2022-04-27 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
