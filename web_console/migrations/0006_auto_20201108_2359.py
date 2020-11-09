# Generated by Django 3.1.dev20200307214613 on 2020-11-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0005_auto_20201108_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birth',
            field=models.DateField(default='2020-11-9'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(default='a@gmail.com', max_length=254, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(default='A', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(default='0214567123', max_length=15),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(default='admin', max_length=20),
        ),
    ]
