from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import UserSerializers, GroupSerializers
from django.contrib.auth.models import User, Group


class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewsets(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
