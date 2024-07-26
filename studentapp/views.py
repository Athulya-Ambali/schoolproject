from datetime import date
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate,login,logout
from adminapp.models import Student, Teacher
from studentapp.forms import StudentLoginForm
from communicationapp.models import Announcement, Notifications
from django.db.models import Q

from teacherapp.models import CourseMaterial

# Create your views here.

class StudentLogin(View):
    def get(self,request):
        form=StudentLoginForm()
        return render(request,'student/studentlogin.html',{'form':form})
    
    def post(self,request):
        if request.method=='POST':
            form=StudentLoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                print(username,password)
                student=authenticate(username=username,password=password)

                print(student)
                if student is not None:
                    login(request,student)
                    return redirect('studentapp:student_profile')
                
                else:
                    msg='error'
                    return render(request,'student/studentlogin.html',{'form':form,'msg':msg})
            
        else:
            form=StudentLoginForm()
        return render(request,'student/studentlogin.html',{'form':form})
    
class StudentProfile(View):
    def get(self,request):
        student = request.user
        
        # Fetching student's details
        stud_ent = Student.objects.get(username=student.username, email=student.email)
        print(f'hhhhhh{stud_ent.course},{stud_ent.batch}')
        s_course = stud_ent.course
        s_batch = stud_ent.batch
        
        # Fetching notifications related to the student's course and batch
        today = date.today()
        teacher = Teacher.objects.get(course=s_course, batch=s_batch)
        files=CourseMaterial.objects.filter(course=s_course,batch=s_batch)
        print(teacher)
        notifications = Notifications.objects.filter(Q(Q(teacher=teacher) | Q(teacher__isnull=True)) & Q(expiry_date__gte=today))
        
        # Calculating reminders for expiring notifications
        reminders = []
        for notif in notifications:
            days = (notif.expiry_date - today).days
            if 0 <= days <= 5:
                reminders.append((notif, days))
        
        return render(request, 'student/student_profile.html', {
            'student': student,
            'stud_ent':stud_ent,
            'notifications': notifications,
            'reminders': reminders,
             'files':files,
        })

        
    
class StudentLogout(View):
    def get(self,request):
        logout(request)
        return redirect('studentapp:student_login')
    

#----------------------------------------Announcement view--------------------------


class AnnouncementView(View):
    def get(self,request):
        announcements=Announcement.objects.all()
        return render(request,'student/announcement_view.html',{'announcements':announcements}) 
    


#----------------------------------------Notification Reminder for students--------------------------


class NotificationReminder(View):
    def get(self, request):
        student = request.user
        # Fetching student's details
        stud_ent = Student.objects.get(username=student.username, email=student.email)
        s_course = stud_ent.course
        s_batch = stud_ent.batch
        
        # Fetching notifications related to the student's course and batch
        today = date.today()
        teacher = Teacher.objects.get(course=s_course, batch=s_batch)
        notifications = Notifications.objects.filter(Q(Q(teacher=teacher) | Q(teacher__isnull=True)) & Q(expiry_date__gte=today))
        
        # Calculating reminders for expiring notifications
        reminders = []
        for notif in notifications:
            days = (notif.expiry_date - today).days
            if 0 <= days <= 5:
                reminders.append((notif, days))
        
        return render(request, 'student/student_profile.html', {
            'student': student,
            'notifications': notifications,
            'reminders': reminders,
        })










