from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer, ProfileSerializer


# Create your views here.

class TaskAPIView(generics.ListCreateAPIView, generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all().filter(user=self.request.user.id)
        return queryset


class TaskDetailAPIView(generics.ListAPIView, generics.UpdateAPIView, generics.RetrieveAPIView,
                        generics.DestroyAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all().filter(user=self.request.user.id)
        return queryset


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            data = {
                "user_id": user.id,
                "message": "User registered successfully."
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
