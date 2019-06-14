# Generated by Django 2.2.1 on 2019-06-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excercise', '0011_usertur_is_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.IntegerField(choices=[(1, 'Zly'), (2, 'Kiepski'), (3, 'Sredni'), (4, 'Dobry'), (5, 'Bardzo Dobry')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='usertur',
            name='is_favorite',
        ),
    ]