# Generated by Django 2.0.6 on 2018-12-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_announcements_date_of_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='date_of_announcement',
            field=models.DateTimeField(),
        ),
    ]
