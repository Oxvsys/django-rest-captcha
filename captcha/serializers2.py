from rest_framework import serializers
from rest_captcha.serializers import RestCaptchaSerializer

from captcha.models import User


class UserSerializer(RestCaptchaSerializer, serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'contact', 'address', 'captcha']

    def create(self, validated_data):
        return User.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.address = validated_data.get('address',instance.address)
        instance.captcha = validated_data.get('captcha',instance.captcha)
        instance.save()
        return instance

class CommentSerializer(RestCaptchaSerializer, serializers.Serializer):
    name = serializers.CharField(max_length=200)
    comments = serializers.CharField(max_length=200)