from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from adminapp.forms import StudentForm, TeacherForm
from .models import *
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
import random
from django.utils.dateparse import parse_date
from teacherapp.models import TeacherAttendance
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



# Create your views here.

#-------------------Admin-----------------------------------

class Index(View):
    def get(self,request):
        return render(request,'index.html')

class AdminLogin(View):
    def get(self,request):
        return render(request,'admin_login.html')
    def post(self,request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            admin= AdminDetails.objects.get(username=username, password=password)
            print(admin)
            if admin is not None:
                login(request,admin)
                return redirect('admin_dashboard')
            else:
                msg='Invalid credentials'
                return render(request,'admin_login.html',{'msg':msg})
            

class AdminLogout(View):
    def get(self,request):
        logout(request)
        return redirect('admin_login')
    
    
class AdminDashBoard(View):
    def get(self,request):
        return render(request,'admin_dashboard.html')

#-------------------CRUD on Course-----------------------------------

class CoursePage(View):
    def get(self,request):
        return render(request,'courses.html') 

class AddCourse(View):
    def get(self,request):
        return render(request,'add_course.html')
    
    def post(self,request):
        if request.method=='POST':
            course=request.POST.get('course')
            course_obj=Course.objects.create(course_name=course)
            return redirect('view_course')


# class ViewCourse(View):
#     def get(self, request):
#         courses = cache.get('course_list')
#         if not courses:
#             courses = list(Course.objects.all())
#             cache.set('course_list', courses, 60) # Cache data for 1 minutes
#         return render(request, 'view_course.html', {'courses': courses})

# class ViewCourse(View):
#     def get(self,request):
#         courses=Course.objects.all()
#         return render(request,'view_course.html',{'courses':courses})

@method_decorator(cache_page(60*2),name='dispatch')
class ViewCourse(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'view_course.html', {'courses': courses})
    
class UpdateCourse(View):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        return render(request,'update_course.html',{'course':course})
    
    def post(self,request,id):
        course_obj=Course.objects.get(id=id)
        if request.method=='POST':
            course_obj.course_name=request.POST.get('course')
            course_obj.save()
            return redirect('view_course')
        
class DeleteCourse(View):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()
        return redirect('view_course')

#-------------------CRUD on Batch-----------------------------------
            
class BatchPage(View):
    def get(self,request):
        return render(request,'batch/batch.html') 

class AddBatch(View):
    def get(self,request):
        return render(request,'batch/add_batch.html')
    
    def post(self,request):
        if request.method=='POST':
            batch=request.POST.get('batch')
            batch_obj=Batch.objects.create(batch=batch)
            return redirect('view_batch')
               
    
class ViewBatch(View):
    def get(self,request):
        batches=Batch.objects.all()
        return render(request,'batch/view_batch.html',{'batches':batches})
    
class UpdateBatch(View):
    def get(self,request,id):
        batch=Batch.objects.get(id=id)
        return render(request,'batch/update_batch.html',{'batch':batch})
    
    def post(self,request,id):
        batch_obj=Batch.objects.get(id=id)
        if request.method=='POST':
            batch_obj.batch=request.POST.get('batch')
            batch_obj.save()
            return redirect('view_batch')
        
class DeleteBatch(View):
    def get(self,request,id):
        batch=Batch.objects.get(id=id)
        batch.delete()
        return redirect('view_batch')

#-----------------Dependend dropdown using Ajax------------------------

class LoadStatesView(View):
    def get(self,request,*args,**kwrags):
        countryid=request.GET.get('country_id')
        states=State.objects.filter(country=countryid).all()
        print(states)
        return JsonResponse (list(states.values('id', 'state_name')), safe=False)
    

class LoadCityView(View):
    def get(self,request,*args,**kwrags):
        stateid=request.GET.get('state_id')
        cities=City.objects.filter(state=stateid).all()
        return JsonResponse(list(cities.values('id', 'city_name')), safe=False)

#-----------------Teacher CRUD using Modelforms------------------------
class TeacherPage(View):
    def get(self,request):
        return render(request,'teacher/teachers.html')
    
class AddTeacher(View):
    def get(self,request):
        form=TeacherForm()
        return render(request,'teacher/add_teacher.html',{'form':form})     
    
     
    def post(self,request):
        if request.method=='POST':
            form=TeacherForm(request.POST,request.FILES)
            if form.is_valid():
                name= form.cleaned_data['name']

                user_name=name.lower().replace('','') # Convert name to lowercase and remove spaces
        
                random_number=random.randint(1000,9999)
                password=f'{user_name}{random_number}'  # Create password by combining the username and random number

                teacher=form.save(commit=False) # Create a model instance without saving to the database yet
                teacher.username=user_name
                teacher.password=password
                form.save()   # Save the model instance to the database
                
                #send mail to teacher which contains username and password
                subject='Account Information'
                message=f'Hi {name}\n\n Your Username is :{user_name} and Password is :{password}\n\n Please reset password after first login'
                send_mail_from=settings.EMAIL_HOST_USER
                recipient_list=[form.cleaned_data['email']]
                send_mail(subject,message,send_mail_from,recipient_list)


                return redirect('view_teacher')
            else:
                return HttpResponse('validation failed')
            
            

class TeachersList(View):
    def get(self,request):
        teacher_obj=Teacher.objects.select_related('course','batch','country','state','city').all()
        return render(request,'teacher/view_teacher.html',{'teachers':teacher_obj})
    

class UpdateTeacher(View):
    def get(self,request,id):
        teacher_instance=Teacher.objects.get(id=id)
        form=TeacherForm(instance=teacher_instance)
        return render(request,'teacher/update_teacher.html',{'form':form})
    
    def post(self,request,id):
        teacher_instance=Teacher.objects.get(id=id)
        if request.method=='POST':
            form=TeacherForm(request.POST,request.FILES, instance=teacher_instance)
            if form.is_valid():
                form.save()
                return redirect('view_teacher')
        

class DeleteTeacher(View):
    def get(self,request,id):
        teacher_instance=Teacher.objects.get(id=id)
        teacher_instance.delete()
        return redirect('view_teacher')


#-----------------Student CRUD using Modelforms------------------------

class StudentPage(View):
    def get(self,request):
        return render(request,'student/students.html')
    


class AddStudent(View):
    def get(self,request):
        form=StudentForm()
        return render(request,'student/add_student.html',{'form':form})
    
    def post(self,request):
        if request.method=='POST':
            form=StudentForm(request.POST,request.FILES)
            if form.is_valid():
                name= form.cleaned_data['first_name']

                user_name=name.lower().replace('','') # Convert name to lowercase and remove spaces
        
                random_number=random.randint(1000,9999)
                password=f'{user_name}{random_number}'  # Create password by combining the username and random number

                student=form.save(commit=False) # Create a model instance without saving to the database yet
                student.username=user_name
                student.set_password(password) #it is saved as hashed passed(so we can aunthenticate it)
                form.save()   # Save the model instance to the database
                
                #send mail to student which contains username and password
                subject='Account Information'
                message=f'Hi {name}\n\n Your Username is :{user_name} and Password is :{password}\n\n Please reset password after first login'
                send_mail_from=settings.EMAIL_HOST_USER
                recipient_list=[form.cleaned_data['email']]
                send_mail(subject,message,send_mail_from,recipient_list)


                return redirect('view_student')
            else:
                return HttpResponse('validation failed')
            

class StudentsList(View):
    def get(self,request):
        student_obj=Student.objects.select_related('course','batch','country','state','city').all()
        return render(request,'student/view_student.html',{'students':student_obj})
            

class UpdateStudent(View):
    def get(self,request,id):
        student_instance=Student.objects.get(id=id)
        form=StudentForm(instance=student_instance)
        return render(request,'student/update_student.html',{'form':form})
    
    def post(self,request,id):
        student_instance=Student.objects.get(id=id)
        if request.method=='POST':
            form=StudentForm(request.POST,request.FILES,instance=student_instance)
            if form.is_valid():
                form.save()
                return redirect('view_student')
            else:
                return HttpResponse('validation failed')


class DeleteStudent(View):
    def get(self,request,id):
        student_instance=Student.objects.get(id=id)
        student_instance.delete()
        return redirect('view_student')
    





#----------------- Teacher Attendance Report ------------------------


class AttendanceReportView(View):
    def get(self, request):
        teachers=Teacher.objects.all()
        return render(request, 'teacherAttendance/attendance_report.html',{'teachers':teachers})

    def post(self, request):
        teachers=Teacher.objects.all()
        start_date = parse_date(request.POST.get('start_date'))
        end_date = parse_date(request.POST.get('end_date'))
        teacher_id = request.POST.get('teacher_id')

        if start_date and end_date:
            if teacher_id:
                attendances = TeacherAttendance.objects.filter(date__range=[start_date, end_date], teacher_name_id=teacher_id)
            else:
                attendances = TeacherAttendance.objects.filter(date__range=[start_date, end_date])
        else:
            attendances = TeacherAttendance.objects.none()

        return render(request, 'teacherAttendance/attendance_report.html', {
            'attendances': attendances,
            'start_date': start_date,
            'end_date': end_date,
            'teacher_id': teacher_id,
            'teachers':teachers
            
        })




