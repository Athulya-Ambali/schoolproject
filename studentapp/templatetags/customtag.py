from django import template
from teacherapp.models import CourseMaterial

register = template.Library()

@register.simple_tag
def get_file_name(id):
    upload_file=CourseMaterial.objects.get(id=id)
    
    return upload_file.title