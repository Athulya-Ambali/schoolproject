from django.http import  HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Announcement
from .forms import AnnouncementForm,NotificationForm
from django.utils import timezone
from .models import Teacher,Notifications
from adminapp.models import Student
from django.db.models import Q

# Create your views here.

#---------------------------------------- Announcements ---------------------------------------

class AnnouncementListView(View):
    def get(self, request):
        announcements = Announcement.objects.all()
        return render(request, 'announcements/announcements.html', {'announcements': announcements})
    
    

class AnnouncementCreateView(View):
    def get(self, request):
        form = AnnouncementForm()
        return render(request, 'announcements/create_announcement.html', {'form': form})
    
    def post(self, request):
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
        return render(request, 'announcements/create_announcement.html', {'form': form})
    


class AnnouncementDetailView(View):
    def get(self, request, pk):
        announcement = Announcement.objects.get(pk=pk)
        return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})
    


class AnnouncementUpdateView(View):
    def get(self, request, pk):
        announcement = Announcement.objects.get(pk=pk)
        form = AnnouncementForm(instance=announcement)
        return render(request, 'announcements/update_announcement.html', {'form': form, 'announcement': announcement})
    
    def post(self, request, pk):
        announcement = Announcement.objects.get(pk=pk)
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
        return render(request, 'announcements/update_announcement.html', {'form': form, 'announcement': announcement})
    


class AnnouncementDeleteView(View):
    def get(self, request, pk):
        announcement = Announcement.objects.get(pk=pk)
        announcement.delete()
        return redirect('announcement_list')


class AnnouncementsDahboardListView(View):
    def get(self, request):
        today=timezone.now().date()
        announcements = Announcement.objects.filter(expiry_date__gte=today)
        return render(request, 'dashboard_announcement.html', {'announcements': announcements})
    
    
#---------------------------------------- Notification ---------------------------------------


class NotificationView(View):
    def get(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page if the user is not authenticated

        student = request.user

        
        # Fetch student entity
        try:
            stud_ent = Student.objects.get(username=student.username, email=student.email)
        except Student.DoesNotExist:
            # Handle the case where the student is not found
            return render(request, 'notifications/error.html', {'message': 'Student not found'})

        # Get the student's course and batch
        s_course = stud_ent.course
        s_batch = stud_ent.batch

        # Fetch the teachers
        teachers = Teacher.objects.filter(course=s_course, batch=s_batch)
        

        if not teachers.exists():
            # Handle the case where no teachers are found
            notifications = Notifications.objects.filter(teacher__isnull=True)
        else:
            # Fetch notifications for the specific teachers or for all (teacher=null)
            notifications = Notifications.objects.filter(Q(teacher__in=teachers) | Q(teacher__isnull=True))
            # Filter notifications based on expiry date
            print(notifications)
            
            notifications = notifications.filter(expiry_date__gte=timezone.now())

        # Return the response
        return render(request, 'notifications/notifications.html', {'student': student, 'notifications': notifications})
    

class CreateNotificationView(View):
    def get(self, request):
      
       
        # Instantiate the NotificationForm to render the form in the template
        form = NotificationForm()
        return render(request, 'notifications/create_notification.html', {'form': form})

    def post(self, request):
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        return render(request, 'notifications/create_notification.html', {'form': form})
    

class UpdateNotificationView(View):
    def get(self, request, pk):
        
        notification = get_object_or_404(Notifications, pk=pk)
        form = NotificationForm(instance=notification)
        return render(request, 'notifications/update_notification.html', {'form': form, 'notification': notification})
    
    def post(self, request, pk):
        
        notification = get_object_or_404(Notifications, pk=pk)
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')  # Redirect to notifications view after successful update
        return render(request, 'notifications/update_notification.html', {'form': form, 'notification': notification})
    

class DeleteNotificationView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('teacherapp:teacher_login')  # Redirect to login page if the user is not authenticated
        
        notification = get_object_or_404(Notifications, pk=pk)
        return render(request, 'notifications/delete_notification.html', {'notification': notification})
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('teacherapp:teacher_login')  # Redirect to login page if the user is not authenticated
        
        notification = get_object_or_404(Notifications, pk=pk)
        notification.delete()
        return HttpResponse('Success')  # Redirect to notifications view after successful deletion



class NotificationTeacherView(View):
    def get(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            # Return an HttpResponse with the error message
            return HttpResponse('Teacher not found', status=404)

        # Fetch notifications for the specific teacher or for all (teacher=null)
        notifications = Notifications.objects.filter(Q(teacher=teacher) | Q(teacher__isnull=True))

        # Render the template with the teacher and notifications
        return render(request, 'notifications/teacher_notifications.html', {'teacher': teacher, 'notifications': notifications})
    


