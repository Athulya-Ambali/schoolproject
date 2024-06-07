from django.urls import path
from communicationapp.views import *

urlpatterns = [
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('announcementdasgboard',AnnouncementsDahboardListView.as_view(),name='announcement_dashboard'),

    path('notifications/', NotificationView.as_view(), name='notifications'),
    path('notificationsCreate/', CreateNotificationView.as_view(), name='create_notification'),
    path('notificationsUpdate/<int:pk>/', UpdateNotificationView.as_view(), name='update_notification'),
    path('notificationsDelete/<int:pk>/', DeleteNotificationView.as_view(), name='delete_notification'),
    path('teacher_notifications/<int:id>/', NotificationTeacherView.as_view(), name='teacher_notifications'),
]
