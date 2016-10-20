from rest_framework import generics
from django.shortcuts import render
from .serializers import CustomUserSerializer
from .models import CustomUser


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

