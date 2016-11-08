from rest_framework import serializers
from .models import Student
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    # students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    
    class Meta:
        model = CustomUser
        # fields = ('id', 'username', 'students')

class StudentSerializer(serializers.ModelSerializer):
    teacher = CustomUserSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
		model = Student
		# fields = ('id', 'name','teacher','phone')






