# Generated by Django 4.2.4 on 2023-10-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0026_alter_userbookpage_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_verfied',
            new_name='is_verified',
        ),
        migrations.AlterField(
            model_name='userbookpage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
