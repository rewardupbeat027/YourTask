from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import TaskAPIView, TaskDetailAPIView, UserRegistrationView

urlpatterns = [
    path('api/v1/tasks/', TaskAPIView.as_view(), name='tasks'),
    path('api/v1/tasks/<int:pk>', TaskDetailAPIView.as_view(), name='detail'),
    path('api/registration/', UserRegistrationView.as_view(), name='registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
