from django.urls import path

from .views import TaskAPIView, TaskDetailAPIView, UserRegistrationView

urlpatterns = [
    path('api/v1/tasks/', TaskAPIView.as_view(), name='tasks'),
    path('api/v1/tasks/<int:pk>', TaskDetailAPIView.as_view(), name='detail'),
    path('api/registration/', UserRegistrationView.as_view(), name='registration'),
]