# Generated by Django 2.1.1 on 2018-11-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181103_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.CharField(max_length=120, unique=True, verbose_name='用户ID'),
        ),
    ]