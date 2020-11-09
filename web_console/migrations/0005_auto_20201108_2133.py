# Generated by Django 3.1.dev20200307214613 on 2020-11-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0004_users_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdetails',
            name='bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='roomType',
            field=models.CharField(choices=[('Phòng trọ', 'Phòng trọ'), ('Chung cư mini', 'Chung cư mini'), ('Chung cư', 'Chung cư'), ('Nhà nguyên căn', 'Nhà nguyên căn')], max_length=100),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='status',
            field=models.CharField(choices=[('Chưa cho thuê', 'Available'), ('Đã cho thuê', 'notAvailable')], max_length=20),
        ),
    ]