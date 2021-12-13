from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import ActivityLog

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return obj.auth_token.key

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ActivityLogSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = ActivityLog
        fields = '__all__'
