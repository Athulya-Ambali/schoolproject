from django.urls import path
from .views import TeacherLogin,TeacherProfile,TeacherLogout,PasswordResetManually,LoginEmailOtp,OtpVerification,AddCourseMaterial,CourseMaterialList,UpdateCourseMaterial,DeleteCourseMaterial,MarkAttendanceView,AttendanceSuccessView,UpdateAttendanceView, DeleteAttendanceView,ViewStudents
app_name='teacherapp'


urlpatterns=[
    path('teacherlogin',TeacherLogin.as_view(),name='teacher_login'),
    path('teacherprofile',TeacherProfile.as_view(),name='teacher_profile'),
    path('teacherlogout',TeacherLogout.as_view(),name='teacher_logout'),
    path('passwordresetmanually/<int:id>',PasswordResetManually.as_view(),name='password_reset_manually'),


    path('login-email-otp/', LoginEmailOtp.as_view(), name='login_email_otp'),
    path('enter-otp/',OtpVerification.as_view(), name='enter_otp'),
    path('verify-otp/',OtpVerification.as_view(),name='otp_verify'),


    path('fileadd/', AddCourseMaterial.as_view(), name='add_course_material'),
    path('fileslist/', CourseMaterialList.as_view(), name='course_material_list'),
    path('update/<int:id>/', UpdateCourseMaterial.as_view(), name='update_course_material'),
    path('delete/<int:id>/', DeleteCourseMaterial.as_view(), name='delete_course_material'),


    path('mark-attendance/', MarkAttendanceView.as_view(), name='mark-attendance'),
    path('attendance-success/', AttendanceSuccessView.as_view(), name='attendance-success'),
    path('update-attendance/<int:pk>/', UpdateAttendanceView.as_view(), name='update_attendance'),
    path('delete-attendance/<int:pk>/', DeleteAttendanceView.as_view(), name='delete_attendance'),

    path('viewstudents/<int:course>/<int:batch>/',ViewStudents.as_view(),name='view_students'),
    
]
