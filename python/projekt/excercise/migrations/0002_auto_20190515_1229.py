# Generated by Django 2.2.1 on 2019-05-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excercise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnament',
            name='turnament_date',
        ),
        migrations.AddField(
            model_name='turnament',
            name='turnament_date_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='turnament',
            name='turnament_date_start',
            field=models.DateField(null=True),
        ),
    ]