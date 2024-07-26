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
        widgets = {
            'sub1': forms.Select(attrs={'class': 'subject-select', 'id': 'id_sub1'}),
            'sub2': forms.Select(attrs={'class': 'subject-select', 'id': 'id_sub2'}),
            'sub3': forms.Select(attrs={'class': 'subject-select', 'id': 'id_sub3'}),
            'sub4': forms.Select(attrs={'class': 'subject-select', 'id': 'id_sub4'}),
            'sub5': forms.Select(attrs={'class': 'subject-select', 'id': 'id_sub5'}),
        }
        
class Excelform(forms.Form):
    file=forms.FileField()