from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
	teacher = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Student
		field = ('id', 'name','teacher')


class TeacherSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'students')