from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import BookSerializers
from .models import Book


class BookViewsets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
