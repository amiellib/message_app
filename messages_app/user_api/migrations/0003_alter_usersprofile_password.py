# Generated by Django 3.2.10 on 2022-11-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_alter_usersprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
