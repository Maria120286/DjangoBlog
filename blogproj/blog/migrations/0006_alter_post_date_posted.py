# Generated by Django 5.0.6 on 2024-06-05 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 11, 16, 53, 194897, tzinfo=datetime.timezone.utc)),
        ),
    ]