# Generated by Django 4.2.4 on 2023-10-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0025_userbook_pages_userbookpage_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookpage',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]
