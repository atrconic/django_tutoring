from rest_framework import serializers
from .models import Course, Class, Student, Mentor


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    class Meta:
        model = Student
        fields = ("__all__")

class CourseSerializer(serializers.ModelSerializer):
    course_description = serializers.CharField(max_length=200)
    student = serializers.CharField(max_length=50)
    mentor = serializers.CharField(max_length=50)
    class_quantity = serializers.IntegerField(default=1, required=False)

    class Meta:
        model = Course
        fields = ("__all__")


class ClassSerializer(serializers.ModelSerializer):
    class_description = serializers.CharField(max_length=200)
    class_price = serializers.FloatField()
    class_duration = serializers.FloatField()
    date_time = serializers.DateTimeField()
    paid = serializers.BooleanField()
    # student = StudentSerializer()
    # def create(self, validated_data):


    class Meta:
        model = Class
        fields = ("__all__")
