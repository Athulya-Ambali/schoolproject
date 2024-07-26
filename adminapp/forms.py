from django import forms
from adminapp.models import *

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['name','mobile','email','course','batch','country','state','city','image']
        # fields='__all__'


class StudentForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
          ] 
     # here we set how much radio buttons needed for an option, value which to save and label to show.
       # in the above example ('male':'Male') male= value to save, Male= label to show.

    # Define the gender field with RadioSelect widget
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, required=False)
    
    # define custom fields
    class Meta:
        model=Student
        fields=['first_name','last_name','email','dob','gender','mobile','address','father_name','course','batch','country','state','city','image']