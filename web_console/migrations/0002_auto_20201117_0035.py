# Generated by Django 3.1.dev20200307214613 on 2020-11-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetails',
            name='comment',
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='roomAddress',
            field=models.CharField(default='', max_length=150),
        ),
    ]