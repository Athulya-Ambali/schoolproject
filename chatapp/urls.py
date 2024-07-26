from django.urls import path
from .views import Chat
app_name='chatapp'

urlpatterns = [

    path('',Chat.as_view(), name='chat'),
   
]