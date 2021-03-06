# Generated by Django 2.1.1 on 2018-10-31 08:39

import apps.user.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('fileID', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='文件ID')),
                ('file', models.FileField(upload_to=apps.user.models.user_data_path, verbose_name='用户上传文件')),
                ('fileStats', models.CharField(default='正在计算.......', max_length=20, verbose_name='文件状态')),
                ('fileScore', models.FloatField(null=True, verbose_name='文件得分')),
            ],
            options={
                'verbose_name': '文件表',
                'db_table': 'Files',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='队伍ID')),
                ('groupName', models.CharField(max_length=20, verbose_name='队伍名称')),
                ('groupCount', models.IntegerField(default=1, verbose_name='队伍人数')),
            ],
            options={
                'verbose_name': '队伍表',
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='GroupGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
                ('groupScore', models.FloatField(verbose_name='得分')),
            ],
            options={
                'verbose_name': '队伍得分表',
                'db_table': 'GroupGrade',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('groupID', models.CharField(default='', max_length=20, verbose_name='所在队伍ID')),
                ('userName', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('passWord', models.CharField(max_length=16, validators=[apps.user.models.validate_even], verbose_name='用户密码')),
                ('userEmail', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('userPhone', models.BigIntegerField(verbose_name='手机')),
                ('userSex', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=4, verbose_name='性别')),
                ('userNo', models.CharField(max_length=11, verbose_name='学号')),
                ('userSchool', models.CharField(max_length=10, verbose_name='学校')),
                ('userStats', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'Users',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['userID'], name='Users_userID_80d74e_idx'),
        ),
        migrations.AddField(
            model_name='groupgrade',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Group', verbose_name='队伍ID'),
        ),
        migrations.AddField(
            model_name='group',
            name='groupHeadID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='队长ID'),
        ),
        migrations.AddField(
            model_name='filemodel',
            name='uploadGroupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Group', verbose_name='所属队伍'),
        ),
        migrations.AddField(
            model_name='filemodel',
            name='uploadUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='提交人ID'),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['groupID'], name='Groups_groupID_bd25c9_idx'),
        ),
    ]
