from django import forms
from .models import *

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
class ReportcardForm(forms.ModelForm):
    class Meta:
        model = Reportcard
        fields = ['stuname', 'sub1', 'mark1', 'sub2', 'mark2', 'sub3', 'mark3', 'sub4', 'mark4', 'sub5', 'mark5']