# Generated by Django 3.1.dev20200307214613 on 2020-11-05 03:01

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner_id', models.IntegerField()),
                ('renter_id', models.IntegerField()),
                ('room_id', models.IntegerField()),
                ('rental_date', models.DateField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_id', models.IntegerField()),
                ('owner_id', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomDescription',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('area', models.FloatField()),
                ('bathroom', models.IntegerField()),
                ('kitchen', models.IntegerField()),
                ('air_conditioning', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('waterPrice', models.IntegerField()),
                ('electricPrice', models.IntegerField()),
                ('postDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('roomAddress', models.TextField()),
                ('roomType', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('owner_id', models.IntegerField()),
                ('comment', models.TextField()),
                ('status', models.BooleanField()),
                ('image1', models.ImageField(default=None, upload_to='pictures/')),
                ('image2', models.ImageField(default=None, upload_to='pictures/')),
                ('image3', models.ImageField(default=None, upload_to='pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(default='', max_length=200)),
                ('user_type', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]