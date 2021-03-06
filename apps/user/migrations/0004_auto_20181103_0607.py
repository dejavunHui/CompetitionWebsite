# Generated by Django 2.1.1 on 2018-11-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181103_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='uploadUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', to_field='userID', verbose_name='提交人ID'),
        ),
        migrations.AlterField(
            model_name='group',
            name='groupHeadID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', to_field='userID', verbose_name='队长ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户ID'),
        ),
    ]
