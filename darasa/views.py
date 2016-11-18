from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
    )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    )

from .serializers import StudentSerializer, TeacherSerializer
from .models import Student
from users.models import CustomUser
from .permissions import IsTeacherOrReadOnly
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets

from django.http import HttpResponseRedirect
from django.shortcuts import render

class ListCreateStudent(generics.ListCreateAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['name', 'phone', 'owner__username']
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,
                      IsTeacherOrReadOnly,
                      )
    
    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'students': serializer.data})

    def get_queryset(self, *args , **kwargs):
        queryset_list = Student.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)|
                Q(phone__icontains=query)|
                Q(owner__username__icontains=query)
                ).distinct()

        return queryset_list

    
    def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	permission_classes = (IsAuthenticated,
                      IsTeacherOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)


class ListCreateTeacher(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TeacherSerializer


class DetailTeacher(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TeacherSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'teachers': reverse('teacher-list', request=request, format=format),
        'students': reverse('student-list', request=request, format=format),
    })

