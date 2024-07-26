from django.shortcuts import render
from django.views import View

# Create your views here.

class Chat(View):
    def get(self,request):
        return render(request,'chat/chat.html')