from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
