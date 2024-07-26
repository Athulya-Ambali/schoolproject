from attr import fields
from django import forms
from adminapp.models import Teacher
from teacherapp.models import CourseMaterial
from .models import TeacherAttendance
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class TeacherLoginForm(forms.ModelForm):
    captcha=ReCaptchaField(widget=ReCaptchaV3)
    
    class Meta:
        model=Teacher
        fields=['username','password','captcha']


class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ['title', 'file','batch','course']


class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['date', 'teacher_name', 'arrival_time', 'departure_time', 'break_start_time', 'break_end_time']


