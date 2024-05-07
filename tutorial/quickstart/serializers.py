from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializers(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'password']

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        instance = User.objects.create_superuser(username=username, password=password)
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
