from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(required=False)
    telegram_id = serializers.IntegerField(required=False)
    token = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        print(*validated_data)
        message = Message(**validated_data)
        message.save()
        return message

