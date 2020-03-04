from django.contrib import admin
from .models import *

"""
    关联对象注册
    可以继承的父类:
    1-层叠显示:admin.TabularInline
    2-表格显示:admin.StackedInline
"""
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
     # 1、列表页属性
     # 显示字段：可以点击列头进行排序
     list_display = ['id', 'bname', 'bimg', 'bpub_date']
     # 过滤字段：过滤框会出现在右侧
     list_filter = ['bname']
     # 搜索字段：搜索框会出现在上侧
     search_fields = ['bname']
     # 分页：分页框会出现在下侧
     list_per_page = 10

     # 2、修改、添加页属性
     # 属性分组
     fieldsets = [
         ('图书名称', {'fields': ['bname']}),
         ('发布时间', {'fields': ['bpub_date']}),
         ('图书版面', {'fields': ['bimg']}),
     ]
     # 关联的对象
     inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
     # 显示字段：可以点击列头进行排序
     list_display = ['id', 'hname', 'gender', 'hcontent', 'hrelation']

# Register your models here.
# 如果需要通过/admin进行管理，需要进行注册
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
