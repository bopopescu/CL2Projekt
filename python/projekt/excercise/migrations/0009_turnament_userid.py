# Generated by Django 2.2.1 on 2019-05-23 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('excercise', '0008_delete_newtur'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnament',
            name='userid',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]