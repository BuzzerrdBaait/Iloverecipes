# Generated by Django 4.2.4 on 2023-10-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_rename_is_verfied_userprofile_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_pic',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics'),
        ),
    ]
