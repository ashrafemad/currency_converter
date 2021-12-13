from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from users.models import ActivityLog
from users.permissions import IsStaffOrSuperUser
from users.serializers import UserSerializer, ActivityLogSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class ActivityLogView(GenericViewSet, ListModelMixin):
    permission_classes = (IsStaffOrSuperUser,)
    serializer_class = ActivityLogSerializer
    queryset = ActivityLog.objects.all()
