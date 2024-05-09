from django.db import models
from datetime import date


# Create your models here.

# 1.新建应用book
# 2.新建模型类Book(title char unique 必填, author char 必填, info char 可以为空)
# 3.新建Book的超连接模型序列化类
# 4.新建Book的模型视图集合
# 5.新建在默认路由中注册books资源
# 6.在apifox中编写关于Book资源的api， 获取列表，创建书籍，获取书籍详细信息，修改书籍信息，删除书籍
# 7.扩展： 自定义Book序列化类继承 Serializer 类实现自定义序列化

class Book(models.Model):
    title = models.CharField("书名", max_length=20, unique=True, null=False, blank=False)

    author = models.CharField("作者名", max_length=10, null=False, blank=False)

    info = models.CharField("简介", max_length=50, null=True, blank=True)

    pub_date = models.DateField("发布时间", default=date(2002, 1, 1))

    category = models.ForeignKey(to="Category", default='2', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField("分类名", max_length=20, unique=True, null=False, blank=False)

    info = models.CharField("简介", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
