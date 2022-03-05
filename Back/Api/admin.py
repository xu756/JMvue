from django.contrib import admin
from .models import *
# Register your models here.

#用户
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'rid')


admin.site.register(User, UserAdmin)
#项目
class UserprojectAdmin(admin.ModelAdmin):
    list_display=('id','ProjectName','fid')
admin.site.register(Userproject,UserprojectAdmin)