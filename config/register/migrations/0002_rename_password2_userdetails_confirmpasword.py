# Generated by Django 3.2 on 2021-05-02 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='password2',
            new_name='ConfirmPasword',
        ),
    ]
