from django.contrib import admin
from .models import User,Group,GroupGrade,FileModel
# Register your models here.


admin.site.register(User)
admin.site.register(Group)
admin.site.register(GroupGrade)
admin.site.register(FileModel)
