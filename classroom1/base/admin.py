from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(student) 
admin.site.register(professor)  
admin.site.register(course)
admin.site.register(stu_course)   