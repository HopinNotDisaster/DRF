from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .serializers import *
from .models import *


# class BookViewsets(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers



def category_list(req):
    """
    获取所有分类和新增分类
    :param req:
    :return:
    """
    if req.method == 'GET':
        categorys = Category.objects.all()
        seria = CategorySerializers(instance=categorys, many=True, context={'request': req})

        return JsonResponse({
            'code': 0,
            'msg': '获取category列表',
            "data": seria.data
        })

    elif req.method == "POST":
        seria = CategorySerializers(data=req.POST, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return JsonResponse({
            'code': 0,
            'msg': '新增category',
            "data": seria.data
        })


def category_detail(req, id):
    pass

    """
    获取category
    删除category
    修改category
    :param req:
    :param bid:
    :return:
    """
    category = get_object_or_404(Category, id=id)
    if req.method == 'GET':
        seria = CategorySerializers(instance=category, context={'request': req})
        return JsonResponse({
            'code': 0,
            'msg': '获取指定category',
            'data': seria.data
        })
    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        seria = CategorySerializers(instance=category, data=data, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return JsonResponse({
            'code': 0,
            'msg': '修改指定category',
            'data': seria.data
        })
    elif req.method == "DELETE":
        category.delete()
        return JsonResponse({
            'code': 0,
            'msg': '删除指定category',
        })







def book_list(req):
    """
    对books发起请求只有两种
    获取所有书和新增书
    :param req:
    :return:
    """
    if req.method == 'GET':
        books = Book.objects.all()
        seria = BookSerializers(instance=books, many=True, context={'request': req})

        return JsonResponse({
            'code': 0,
            'msg': '获取书籍列表',
            "data": seria.data
        })

    elif req.method == "POST":
        seria = BookSerializers(data=req.POST, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return JsonResponse({
            'code': 0,
            'msg': '新增书籍',
            "data": seria.data
        })


def book_detail(req, id):
    """
    获取书
    删除书
    修改书
    :param req:
    :param bid:
    :return:
    """
    book = get_object_or_404(Book, id=id)
    if req.method == 'GET':
        seria = BookSerializers(instance=book, context={'request': req})
        return JsonResponse({
            'code': 0,
            'msg': '获取指定书籍',
            'data': seria.data
        })
    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        seria = BookSerializers(instance=book, data=data, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return JsonResponse({
            'code': 0,
            'msg': '修改指定书籍',
            'data': seria.data
        })
    elif req.method == "DELETE":
        book.delete()
        return JsonResponse({
            'code': 0,
            'msg': '删除指定书籍',
        })
