from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class BookViewsets(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    @action(["get"], detail=False)
    def top3(self, req):
        books_top3 = Book.objects.order_by("-pub_date")[0:3]
        seria = BookSerializers(instance=books_top3, many=True, context={'request': req})
        return Response(data={
            'code': 0,
            'msg': '获取前三本书列表',
            "data": seria.data
        }, status=status.HTTP_200_OK)


class CategoryViewsets(viewsets.ModelViewSet):
    lookup_field = "id"

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

# @api_view(["GET", "POST", ])
# def category_list(req):
#     if req.method == 'GET':
#         categorys = Category.objects.all()
#         seria = CategorySerializers(instance=categorys, many=True, context={'request': req})
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '获取category列表',
#         #     "data": seria.data
#         # })
#         return Response(data={
#             'code': 0,
#             'msg': '获取category列表',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     elif req.method == "POST":
#         seria = CategorySerializers(data=req.POST, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '新增category',
#         #     "data": seria.data
#         # })
#         return Response(data={
#             'code': 0,
#             'msg': '新增category',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def category_detail(req, id):
#     category = get_object_or_404(Category, id=id)
#     if req.method == 'GET':
#         seria = CategorySerializers(instance=category, context={'request': req})
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '获取指定category',
#         #     'data': seria.data
#         # })
#         return Response(data={
#             'code': 0,
#             'msg': '获取指定category',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     elif req.method == 'PUT':
#         # data = JSONParser().parse(req)
#         data = req.POST
#         seria = CategorySerializers(instance=category, data=data, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '修改指定category',
#         #     'data': seria.data
#         # })
#
#         return Response(data={
#             'code': 0,
#             'msg': '修改指定category',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#     elif req.method == "DELETE":
#         category.delete()
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '删除指定category',
#         # })
#         return Response(data={
#             'code': 0,
#             'msg': '删除指定category',
#         }, status=status.HTTP_200_OK)
#
#
# @api_view(["GET", "POST"])
# def book_list(req):
#     """
#     对books发起请求只有两种
#     获取所有书和新增书
#     :param req:
#     :return:
#     """
#     if req.method == 'GET':
#         books = Book.objects.all()
#         seria = BookSerializers(instance=books, many=True, context={'request': req})
#
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '获取书籍列表',
#         #     "data": seria.data
#         # })
#
#         return Response(data={
#             'code': 0,
#             'msg': '获取书籍列表',
#             "data": seria.data
#         }, status=status.HTTP_200_OK)
#
#     elif req.method == "POST":
#         seria = BookSerializers(data=req.POST, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return JsonResponse({
#             'code': 0,
#             'msg': '新增书籍',
#             "data": seria.data
#         })
#
#
# def book_detail(req, id):
#     book = get_object_or_404(Book, id=id)
#     if req.method == 'GET':
#         seria = BookSerializers(instance=book, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取指定book',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#     elif req.method == 'PUT':
#         data = JSONParser().parse(req)
#         seria = BookSerializers(instance=book, data=data, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(data={
#             'code': 0,
#             'msg': '修改指定book',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#     elif req.method == "DELETE":
#         book.delete()
#         return Response(data={
#             'code': 0,
#             'msg': '删除指定book',
#         }, status=status.HTTP_200_OK)

#
# class CategoryListView(APIView):
#     def get(self, req):
#         categorys = Category.objects.all()
#         seria = CategorySerializers(instance=categorys, many=True, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取category列表',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def post(self, req):
#         seria = CategorySerializers(data=req.POST, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(data={
#             'code': 0,
#             'msg': '新增category',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#
# class CategoryDetailView(APIView):
#     def get(self, req, id):
#         try:
#             category = Category.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         seria = CategorySerializers(instance=category, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取指定category',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def put(self, req, id):
#         try:
#             category = Category.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         data = req.POST
#         seria = CategorySerializers(instance=category, data=data, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(data={
#             'code': 0,
#             'msg': '修改指定category',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def detele(self, id):
#         try:
#             category = Category.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         category.delete()
#         return Response(data={
#             'code': 0,
#             'msg': '删除指定category',
#         }, status=status.HTTP_200_OK)
#

# class BookListView(APIView):
#     def get(self, req):
#         books = Book.objects.all()
#         seria = BookSerializers(instance=books, many=True, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取书籍列表',
#             "data": seria.data
#         }, status=status.HTTP_200_OK)
#
#     def post(self, req):
#         seria = BookSerializers(data=req.POST, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return JsonResponse({
#             'code': 0,
#             'msg': '新增书籍',
#             "data": seria.data
#         })
#
#
# class BookDetailView(APIView):
#     def get(self, req, id):
#         try:
#             book = Book.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         seria = BookSerializers(instance=book, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取指定book',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def put(self, req, id):
#         try:
#             book = Book.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         data = JSONParser().parse(req)
#         seria = BookSerializers(instance=book, data=data, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(data={
#             'code': 0,
#             'msg': '修改指定book',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def delete(self, id):
#         try:
#             book = Book.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         book.delete()
#         return Response(data={
#             'code': 0,
#             'msg': '删除指定book',
#         }, status=status.HTTP_200_OK)

#
# class BookListCreateAPIView(ListCreateAPIView):
#     def get_queryset(self):
#         return Book.objects.all()
#
#     def get_serializer_class(self):
#         return BookSerializers
#
#     # @action(["get"], detail=False)
#     # def top3(self, req):
#     #     books_top3 = Book.objects.order_by("-pub_date")[0:3]
#     #     seria = BookSerializers(instance=books_top3, many=True, context={'request': req})
#     #     return Response(data={
#     #         'code': 0,
#     #         'msg': '获取前三本书列表',
#     #         "data": seria.data
#     #     }, status=status.HTTP_200_OK)
#
#
# class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     lookup_field = "id"
#
#     def get_queryset(self):
#         return Book.objects.all()
#
#     def get_serializer_class(self):
#         return BookSerializers
