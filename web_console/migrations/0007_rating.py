# Generated by Django 3.1.dev20200307214613 on 2020-12-04 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('room_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('rating', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
