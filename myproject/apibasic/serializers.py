from rest_framework import serializers
from .models import FileList
from django.contrib.auth.models import User

class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model=FileList
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user=User.objects.create_user(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        




    
