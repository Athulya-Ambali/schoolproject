
from django.db import models
from adminapp.models import Teacher
from django.utils import timezone 

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date=models.DateField(null=True)
    
    def __str__(self):
        return self.title


class Notifications(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher',null=True,blank=True)
    title=models.CharField(max_length=250)
    message=models.CharField(max_length=500)
    document=models.FileField(upload_to='notifications/',null=True,blank=True)
    posted_date=models.DateField(default=timezone.now)
    expiry_date=models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return f'Notification--{self.title}'




