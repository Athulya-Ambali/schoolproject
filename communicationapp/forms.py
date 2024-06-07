from django import forms
from .models import Announcement,Notifications

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'message','expiry_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
           
        }



class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        
        fields='__all__'
