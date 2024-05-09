from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializers, GroupSerializers
from django.contrib.auth.models import User, Group


# class UserViewsets(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers


# class GroupViewsets(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializers


class UserListView(APIView):
    def get(self, req):
        users = User.objects.all()
        seria = UserSerializers(instance=users, many=True, context={'request': req})
        return Response(data={
            'code': 0,
            'msg': '获取user列表',
            'data': seria.data
        }, status=status.HTTP_200_OK)

    def post(self, req):
        seria = UserSerializers(data=req.POST, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data={
            'code': 0,
            'msg': '新增user',
            'data': seria.data
        }, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, req, id):
        try:
            user = User.objects.get(id=id)
        except:
            return Response({
            }, status=status.HTTP_404_NOT_FOUND)
        seria = UserSerializers(instance=user, context={'request': req})
        return Response(data={
            'code': 0,
            'msg': '获取指定User',
            'data': seria.data
        }, status=status.HTTP_200_OK)

    def put(self, req, id):
        try:
            user = User.objects.get(id=id)
        except:
            return Response({
            }, status=status.HTTP_404_NOT_FOUND)
        data = req.POST
        seria = UserSerializers(instance=user, data=data, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data={
            'code': 0,
            'msg': '修改指定User',
            'data': seria.data
        }, status=status.HTTP_200_OK)

    def detele(self, id):
        try:
            user = User.objects.get(id=id)
        except:
            return Response({
            }, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(data={
            'code': 0,
            'msg': '删除指定User',
        }, status=status.HTTP_200_OK)


# class GroupListView(APIView):
#     def get(self, req):
#         groups = Group.objects.all()
#         seria = GroupSerializers(instance=groups, many=True, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取用户组列表',
#             "data": seria.data
#         }, status=status.HTTP_200_OK)
#
#     def post(self, req):
#         seria = GroupSerializers(data=req.POST, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         # return JsonResponse({
#         #     'code': 0,
#         #     'msg': '新增书籍',
#         #     "data": seria.data
#         # })
#         return Response(data={
#             'code': 0,
#             'msg': '新增用户组列表',
#             "data": seria.data
#         }, status=status.HTTP_200_OK)
#
#
# class GroupDetailView(APIView):
#     def get(self, req, id):
#         try:
#             group = Group.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         seria = GroupSerializers(instance=group, context={'request': req})
#         return Response(data={
#             'code': 0,
#             'msg': '获取指定Group',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def put(self, req, id):
#         try:
#             group = Group.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         data = JSONParser().parse(req)
#         seria = GroupSerializers(instance=group, data=data, context={'request': req})
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(data={
#             'code': 0,
#             'msg': '修改指定Group',
#             'data': seria.data
#         }, status=status.HTTP_200_OK)
#
#     def delete(self, id):
#         try:
#             group = Group.objects.get(id=id)
#         except:
#             return Response({
#             }, status=status.HTTP_404_NOT_FOUND)
#         group.delete()
#         return Response(data={
#             'code': 0,
#             'msg': '删除指定group',
#         }, status=status.HTTP_200_OK)
#


class GroupListGenericView(GenericAPIView):

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_class(self):
        return GroupSerializers

    def get(self, req):
        seria = self.get_serializer(instance=self.get_queryset(), many=True, context={'request': req})
        return Response(data={
            'code': 0,
            'msg': '获取用户组列表',
            "data": seria.data
        }, status=status.HTTP_200_OK)

    def post(self, req):
        seria = self.get_serializer(data=req.POST, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data={
            'code': 0,
            'msg': '新增用户组列表',
            "data": seria.data
        }, status=status.HTTP_200_OK)


class GroupDetailGenericView(GenericAPIView):
    lookup_field = "id"

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_class(self):
        return GroupSerializers

    def get(self, req, id):
        try:
            object = self.get_object()
        except:
            return Response({
            }, status=status.HTTP_404_NOT_FOUND)
        seria = self.get_serializer(instance=object, context={'request': req})
        return Response(data={
            'code': 0,
            'msg': '获取指定Group',
            'data': seria.data
        }, status=status.HTTP_200_OK)

    def put(self, req, id):
        try:
            object = self.get_object()
        except:
            return Response({
            }, status=status.HTTP_404_NOT_FOUND)
        data = JSONParser().parse(req)
        seria = GroupSerializers(instance=object, data=data, context={'request': req})
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data={
            'code': 0,
            'msg': '修改指定Group',
            'data': seria.data
        }, status=status.HTTP_200_OK)

    def delete(self, id):
        try:
            object = self.get_object()
        except:
            return Response({
            }, status=status.HTTP_404_NOT_FOUND)
        object.delete()
        return Response(data={
            'code': 0,
            'msg': '删除指定group',
        }, status=status.HTTP_200_OK)
