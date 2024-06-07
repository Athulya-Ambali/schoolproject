from django.urls import path
from .views import *


urlpatterns=[
    path('',Index.as_view(),name='index'),

    path('adminlogin',AdminLogin.as_view(),name='admin_login'),
    path('admin_dashboard',AdminDashBoard.as_view(),name='admin_dashboard'),
    path('adminlogut',AdminLogout.as_view(),name='admin_logout'),


    path('courses',CoursePage.as_view(),name='courses'),
    path('addcourse',AddCourse.as_view(),name='add_course'),
    path('viewcourse',ViewCourse.as_view(),name='view_course'),
    path('updatecourse/<int:id>',UpdateCourse.as_view(),name='update_course'),
    path('deletecourse/<int:id>',DeleteCourse.as_view(),name='delete_course'),


    path('batches',BatchPage.as_view(),name='batches'),
    path('addbatche',AddBatch.as_view(),name='add_batch'),
    path('viewbatch',ViewBatch.as_view(),name='view_batch'),
    path('updatebatch/<int:id>',UpdateBatch.as_view(),name='update_batch'),
    path('deletebatch/<int:id>',DeleteBatch.as_view(),name='delete_batch'),


    path('teachers',TeacherPage.as_view(),name='teachers'),
    path('addteacher',AddTeacher.as_view(),name='add_teacher'),
    path('viewteacher',TeachersList.as_view(),name='view_teacher'),
    path('updateteacher/<int:id>',UpdateTeacher.as_view(),name='update_teacher'),
    path('dalateteacher/<int:id>',DeleteTeacher.as_view(),name='delete_teacher'),


    path('students',StudentPage.as_view(),name='students'),
    path('addstudent',AddStudent.as_view(),name='add_student'),
    path('viewstudent',StudentsList.as_view(),name='view_student'),
    path('updatestudent/<int:id>',UpdateStudent.as_view(),name='update_student'),
    path('deletestudent/<int:id>',DeleteStudent.as_view(),name='delete_student'),

    path('attendance-report/', AttendanceReportView.as_view(), name='attendance_report'),

    path('liststates',LoadStatesView.as_view(),name='list_states'),
    path('listcities',LoadCityView.as_view(),name='list_cities'),

    
    ]








