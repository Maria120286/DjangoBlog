# Generated by Django 5.0.6 on 2024-06-05 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 9, 48, 1, 800397, tzinfo=datetime.timezone.utc)),
        ),
    ]
