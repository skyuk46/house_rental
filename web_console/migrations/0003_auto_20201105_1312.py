# Generated by Django 3.1.dev20200307214613 on 2020-11-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0002_auto_20201105_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
