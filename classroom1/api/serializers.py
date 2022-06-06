from rest_framework import fields, serializers 
from base.models import student, professor, course, stu_course, prof_course

class studentSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = student
        fields = '__all__' 


class professorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = professor
        fields = '__all__' 


class courseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = course
        fields = '__all__' 


class stuCourseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = stu_course
        fields = '__all__' 


class profCourseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = prof_course
        fields = '__all__' 