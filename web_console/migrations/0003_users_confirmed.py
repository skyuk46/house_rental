# Generated by Django 3.1.dev20200307214613 on 2020-11-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0002_auto_20201117_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
