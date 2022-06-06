from typing import List
from django.db import models
from rest_framework.response import Response 
from rest_framework.views import APIView 
from base.models import *
from .serializers import *
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List and Create Student
class LCStudent(GenericAPIView, ListModelMixin, CreateModelMixin): 
    queryset = student.objects.all() 
    serializer_class = studentSerializer 

    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs) 
    
# Retrieve, Update and Delete Student
class RUDStudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): 
    queryset = student.objects.all() 
    serializer_class = studentSerializer 

    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs) 

    

# List and Create Professor
class LCProfessor(GenericAPIView, ListModelMixin, CreateModelMixin): 
    queryset = professor.objects.all() 
    serializer_class = professorSerializer 

    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs) 
    
# Retrieve, Update and Delete Professor
class RUDProfessor(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): 
    queryset = professor.objects.all() 
    serializer_class = professorSerializer 

    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs) 



# List and Create Course
class LCCourse(GenericAPIView, ListModelMixin, CreateModelMixin): 
    queryset = course.objects.all() 
    serializer_class = courseSerializer 

    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs) 
    
# Retrieve, Update and Delete Course
class RUDCourse(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): 
    queryset = course.objects.all() 
    serializer_class = courseSerializer 

    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs) 



# List and Create Student-Courses
class LCStuCourse(GenericAPIView, ListModelMixin, CreateModelMixin): 
    queryset = stu_course.objects.all() 
    serializer_class = stuCourseSerializer 

    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs) 
    
# Retrieve, Update and Delete Student-Courses
class RUDStuCourse(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): 
    queryset = stu_course.objects.all() 
    serializer_class = stuCourseSerializer 

    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs)



# List and Create Professor-Courses
class LCProfCourse(GenericAPIView, ListModelMixin, CreateModelMixin): 
    queryset = prof_course.objects.all() 
    serializer_class = profCourseSerializer 

    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs) 
    
# Retrieve, Update and Delete Professor-Courses
class RUDProfCourse(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): 
    queryset = prof_course.objects.all() 
    serializer_class = profCourseSerializer 
 

    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs)
























#** METHOD-1 **#
 
# #STUDENT
# class Student(APIView):
#     def get(self, request, format=None):
#         students = student.objects.all() 
#         serializer = studentSerializer(students, many=True)  
#         return Response(serializer.data) 

#     def post(self, request, format=None): 
#         serializer = studentSerializer(data=request.data) 
#         if serializer.is_valid():   
#             serializer.save() 
#         return Response(serializer.data)  


# #PROFESSOR
# class Professor(APIView):
#     def get(self, request, format=None):
#         professors = professor.objects.all() 
#         serializer = professorSerializer(professors, many=True) 
#         return Response(serializer.data)  

#     def post(self, request, format=None):
#         serializer = professorSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save() 
#         return Response(serializer.data)  


# #COURSE
# class Course(APIView):
#     def get(self, request, format=None):
#         courses = course.objects.all() 
#         serializer = courseSerializer(courses, many=True) 
#         return Response(serializer.data) 

#     def post(self, request, format=None):
#         serializer = courseSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save() 
#         return Response(serializer.data)  


# #STU-COURSE 
# class Student_Course(APIView):
#     def get(self, request, format=None):
#         stu_courses = stu_course.objects.all() 
#         serializer = stuCourseSerializer(stu_courses, many=True) 
#         return Response(serializer.data) 

#     def post(self, request, format=None):
#         serializer = stuCourseSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save() 
#         return Response(serializer.data)  