from django.contrib import admin
from .models import Users

# Register your models here.

# 定义一个展示类
class UserAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = ('id','username','age','sex','email','addtime')

    # 设置默认可编辑字段
    list_editable = ['username','age','email']

    # 过滤器
    list_filter = ('username','age','email')

    # 搜索字段
    search_fields = ('username','age','email')

    # 详细时间分成筛选
    date_hierarchy = 'addtime'

    # 排序 负号代表降序
    ordering = ('id',)

    # 分页，可设置每页展示的条数
    list_per_page = 20

# 注册应用
admin.site.register(Users,UserAdmin)
