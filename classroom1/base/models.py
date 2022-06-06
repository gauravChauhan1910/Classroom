from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import module_loading

# Create your models here.

class student(models.Model): 
    roll_no = models.CharField(max_length=16) 
    name = models.CharField(max_length=64) 
    branch = models.CharField(max_length=16) 

    def __str__(self): 
        return f"{self.id}: {self.roll_no}      {self.name}      {self.branch}" 


class professor(models.Model): 
    pname = models.CharField(max_length=64)
    dept = models.CharField(max_length=32) 

    def __str__(self): 
        return f"{self.id}: {self.pname}    {self.dept}" 


class course(models.Model): 
    cname = models.CharField(max_length=32) 

    def __str__(self): 
        return f"{self.id}: {self.cname}" 


class stu_course(models.Model): 
    stu_id = models.ForeignKey(student, on_delete=models.CASCADE) 
    courses = models.ManyToManyField(course, blank=True) 

    def __str__(self): 
        return f"{self.id}:     {self.stu_roll_no}"   


class prof_course(models.Model): 
    prof_id = models.ForeignKey(professor, on_delete=models.CASCADE) 
    courses = models.ManyToManyField(course, blank=True) 

    def __str__(self): 
        return f"{self.id}"     