# Generated by Django 4.1.3 on 2023-02-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Profilepic',
            field=models.FileField(blank=True, null=True, upload_to='user_profile/'),
        ),
    ]
