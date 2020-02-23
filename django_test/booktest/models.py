from django.db import models

"""
models文件的作用：
   1、根据models的定义去生成SQL语句，并创建表
   2、创建对象，对对象进行各种操作
   图书-英雄的关系为一对多
"""
# Create your models here.
class BookInfoManager(models.Manager):
     """
        自定义管理器
     """
     # 情况一：更改默认查询结果,只查未删除的数据
     def get_queryset(self):
         return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

     # 情况二：定义模型类的创建方法
     def create(cls, bname, bpub_date):
         b = BookInfo()
         b.bname = bname
         b.bpub_date = bpub_date
         b.bread = 0
         b.bcomment = 0
         b.isDelete = False
         return b

class BookInfo(models.Model):
    """
        图书类 => 图书表(booktest_bookinfo)
    """
    # 默认自动生成id
    # 图书名称
    bname = models.CharField(max_length=20)
    # 图书发布时间
    bpub_date = models.DateTimeField()
    # 阅读数 => int(11)
    bread = models.IntegerField(default=0)
    # 评论数 => int(11)
    bcomment = models.IntegerField(default=0)
    # 是否删除 => tinyint
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.bname

    # 管理器
    manager1 = models.Manager()
    manager2 = BookInfoManager()
    # 元选项
    class Meta:
        # 数据表名
        db_table = "bookinfo"
        # 对象默认排序字段，正序， 负序带-，如["-id"]
        ordering = ["id"]

class HeroInfo(models.Model):
    """
        英雄类 => 英雄表(booktest_heroinfo)
    """
    # 英雄名称
    hname = models.CharField(max_length=10)
    # 英雄性别
    hgender = models.BooleanField()
    # 英雄简介
    hcontent = models.CharField(max_length=256)
    # 英雄关系
    hrelation = models.CharField(max_length=64)
    # 是否删除 => tinyint
    isDelete = models.BooleanField(default=False)
    # 所属图书： 外键引用对象
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
    def gender(self):
        if self.hgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"