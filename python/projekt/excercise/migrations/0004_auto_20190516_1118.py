# Generated by Django 2.2.1 on 2019-05-16 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excercise', '0003_auto_20190515_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_password',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_description',
        ),
    ]