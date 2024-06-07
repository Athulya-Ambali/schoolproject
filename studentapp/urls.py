from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
app_name='studentapp'

urlpatterns = [
    path('studentlogin',StudentLogin.as_view(),name='student_login'),
    path('studentprofile',StudentProfile.as_view(),name='student_profile'),
    path('Remainder/', NotificationReminder.as_view(), name='notification_reminder'),
    path('announcementstudent/', AnnouncementView.as_view(), name='announcement_student'),
    path('studentlogout',StudentLogout.as_view(),name='student_logout'),
    

    path('password_reset/', auth_view.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]

