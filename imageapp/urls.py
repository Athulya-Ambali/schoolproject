from django.urls import path
from .views import CreateImage, ViewImage

urlpatterns = [
    path('upload/', CreateImage.as_view(), name='upload_image'),
    path('view/', ViewImage.as_view(), name='view_image'),
]
