from django.urls import path 
from . import views 

urlpatterns = [
    path('studentapi/', views.LCStudent.as_view(), name="lcStudent"),  
    path('studentapi/<int:pk>', views.RUDStudent.as_view(), name="rudStudent"), 

    path('professorapi/', views.LCProfessor.as_view(), name="lcProfessor"),  
    path('professorapi/<int:pk>', views.RUDProfessor.as_view(), name="rudProfessor"), 

    path('courseapi/', views.LCCourse.as_view(), name="lcCourse"),  
    path('courseapi/<int:pk>', views.RUDCourse.as_view(), name="rudCourse"), 

    path('stu_courseapi/', views.LCStuCourse.as_view(), name="lcStuCourse"),  
    path('stu_courseapi/<int:pk>', views.RUDStuCourse.as_view(), name="rudStuCourse"),

    path('prof_courseapi/', views.LCProfCourse.as_view(), name="lcProfCourse"),  
    path('prof_courseapi/<int:pk>', views.RUDProfCourse.as_view(), name="rudProfCourse"), 
] 
