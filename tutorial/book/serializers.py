from rest_framework import serializers
from .models import *
from datetime import date


# class BookSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

# 1.在book应用中新建模型类Category（title char unique 必填, info text 可为空）
# 2.新建Category的自定义序列化类
# 3.自定义Category的列表与详情路由
# 4.自定义Category的列表与详情视图函数处理GET、POST、PUT、DELETE
# 5.在apifox中编写关于Category资源的api， 获取分类列表，创建分类，获取分类详细信息，修改分类信息，删除分类
# 6.扩展(使用drf的@api_view 装饰器 与 Response处理请求与响应)

class CategorySerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='category-detail', lookup_field='id')
    title = serializers.CharField(max_length=50)
    info = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.info = validated_data.get('info', '')
        instance.save()
        return instance


class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, )
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='book-detail', lookup_field='id')
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=10)
    pub_date = serializers.DateField(default=date(2002, 1, 1))

    def create(self, validated_data):
        instance = Book.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.author = validated_data.get('author')
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.info = validated_data.get('info', '')
        instance.save()
        return instance
