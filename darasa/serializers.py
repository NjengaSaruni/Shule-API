from rest_framework import serializers
from .models import Student
from users.models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
	teacher = serializers.ReadOnlyField(source='teacher.username')

	class Meta:
		model = Student
		# fields = ('id', 'name','teacher','phone')


class TeacherSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'students')




