from django.contrib import admin
# 现在给后台管理系统 admin 注册用户模型，使其能在后台管理界面直接添加或修改用户数据
# Register your models here.
from .models import User

admin.site.register(User)