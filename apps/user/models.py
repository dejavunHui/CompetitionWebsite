from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


def validate_even(value):
    '''
    验证密码是否符合要求
    :param value:
    :return:
    '''
    if a.isdigit():
        raise ValidationError(
            _('请确保密码包含数字,符号或者字符')
        )
    for i in range(11):
        if str(i) in value:
            break
    if i > 9:
        raise ValidationError(
            _('请确保密码包含数字,符号或者字符')
        )


class User(models.Model):

    userID = models.CharField(
        max_length=20, primary_key=True, verbose_name='用户ID')
    groupID = models.CharField(max_length=20,default='',verbose_name='所在队伍ID')
    userName = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    passWord = models.CharField(max_length=16, validators=[
                                validate_even], verbose_name='用户密码')
    userEmail = models.EmailField(verbose_name='用户邮箱')
    userPhone = models.BigIntegerField(verbose_name='手机')
    userSex = models.CharField(max_length=4,
                               choices=(('m', 'male'),
                                        ('f', 'female')),
                               blank=True, verbose_name='性别')
    userNo = models.CharField(max_length=11,null=False,verbose_name='学号')
    userSchool = models.CharField(max_length=10,verbose_name='学校')
    userStats = models.CharField(max_length=5)

    class Meta:
        db_table = 'Users'#表名
        indexes = [models.Index(fields=['userID'])]
        verbose_name = '用户表'




class Group(models.Model):

    groupID = models.CharField(max_length=20,primary_key=True,verbose_name='队伍ID')
    groupName = models.CharField(max_length=20,verbose_name='队伍名称')
    groupHeadID = models.ForeignKey(User,on_delete=models.CASCADE,to_field='userID',verbose_name='队长ID')
    groupCount = models.IntegerField(default=1,verbose_name='队伍人数')

    class Meta:
        db_table = 'Groups'
        indexes = [models.Index(fields=['groupID'])]
        verbose_name = '队伍表'

class GroupGrade(models.Model):

    groupID = models.ForeignKey(Group, on_delete=models.CASCADE,to_field='groupID',verbose_name='队伍ID')

    Time = models.DateTimeField(auto_now_add=True,verbose_name='提交时间')
    groupScore = models.FloatField(verbose_name='得分')


    class Meta:
        db_table = 'GroupGrade'
        verbose_name = '队伍得分表'


def user_data_path(instance,filename):
    '''
    用户文件上传位置
    '''
    return 'data/user_{0}/{1}'.format(instance.uploadGroupID,filename)


class FileModel(models.Model):

    fileID = models.CharField(max_length=30,verbose_name='文件ID',primary_key=True)
    uploadUserID = models.ForeignKey(User, on_delete=models.CASCADE,to_field='userID',verbose_name='提交人ID')
    uploadGroupID = models.ForeignKey(Group, on_delete=models.CASCADE,to_field='groupID',verbose_name='所属队伍')
    file = models.FileField(upload_to=user_data_path,verbose_name='用户上传文件')
    fileStats = models.CharField(max_length = 20,default='正在计算.......',verbose_name='文件状态')
    fileScore = models.FloatField(verbose_name='文件得分',null=True)

    class Meta:
        db_table = 'Files'
        verbose_name = '文件表'
