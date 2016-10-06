from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import StudentSerializer, TeacherSerializer
from .models import Student
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import viewsets

class ListCreateStudent(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ListCreateTeacher(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer


class DetailTeacher(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'teachers': reverse('teacher-list', request=request, format=format),
        'students': reverse('student-list', request=request, format=format),
    })


# class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = TeacherSerializer

# class StudentViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)