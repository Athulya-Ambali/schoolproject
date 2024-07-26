from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from imageapp.models import UploadedImage
from .forms import ImageForm

# Create your views here.

class CreateImage(View):
    def get(self,request):
        form=ImageForm()
        return render(request,'image/image_upload.html',{'form':form})
    
    def post(self,request):
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Success image is uploaded')
        else:
            return HttpResponse('form validation failed')
        

class ViewImage(View):
    def get(self,request):
        image=UploadedImage.objects.all()
        return render(request,'image/image_view.html',{'image':image})


  