# Generated by Django 2.2.1 on 2019-06-14 14:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('excercise', '0012_auto_20190614_1413'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.AddField(
            model_name='usertur',
            name='mark',
            field=models.IntegerField(choices=[(1, 'Zly'), (2, 'Kiepski'), (3, 'Sredni'), (4, 'Dobry'), (5, 'Bardzo Dobry')], default=0),
        ),
        migrations.AlterUniqueTogether(
            name='usertur',
            unique_together={('user', 'tournament', 'mark')},
        ),
    ]