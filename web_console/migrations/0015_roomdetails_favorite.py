# Generated by Django 3.1.4 on 2020-12-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0014_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdetails',
            name='favorite',
            field=models.IntegerField(default=0),
        ),
    ]