from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from users.views import CreateUserView, ActivityLogView

router = DefaultRouter()
router.register(r'activity-log', ActivityLogView)


urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('obtain-token/', obtain_auth_token),
    path('', include(router.urls)),
]
