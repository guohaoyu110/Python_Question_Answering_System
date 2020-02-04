# Register your models here.
# 个人详情应用模型和表单的编写
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)