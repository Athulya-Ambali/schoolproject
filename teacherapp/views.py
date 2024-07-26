
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from adminapp.models import Student, Teacher
from teacherapp.forms import TeacherLoginForm
from django.contrib.auth import login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from datetime import datetime,timedelta
from .forms import CourseMaterialForm
from .models import CourseMaterial
from .models import TeacherAttendance
from .forms import TeacherAttendanceForm



# Create your views here.



class TeacherLogin(View):
    def get(self,request):
        form=TeacherLoginForm()
        return render(request,'teacher/teacherlogin.html',{'form':form})
    
    def post(self,request):
        if request.method=='POST':
            form=TeacherLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                print(username,password)
                teacher=Teacher.objects.get(username=username,password=password)
                # teacher=authenticate(username=username,password=password)

                print(teacher)

                if teacher is not None:
                    login(request,teacher)
                    return render(request,'teacher/teacher_profile.html',{'teacher':teacher})
            
                else:
                    msg='error'
                    return render(request,'teacher/teacherlogin.html',{'form':form,'msg':msg})
        else:
            form=TeacherLoginForm()
        return render(request,'teacher/teacherlogin.html',{'form':form})
            

class TeacherProfile(View):
    def get(self,request):
        return render(request,'teacher/teacher_profile.html')
    
class TeacherLogout(View):
    def get(self,request):
        logout(request)
        return redirect('teacherapp:teacher_login')
    


class PasswordResetManually(View):
    def get(self,request,id):
        return render(request,'teacher/password_reset_manually.html')
    def post(self,request,id):
        msg=''
        teacher_obj=Teacher.objects.get(id=id)
        if request.method=='POST':
            old_password=request.POST.get('old_password')
            new_password=request.POST.get('new_password')
            confirm_password=request.POST.get('confirm_password')
            if teacher_obj.password==old_password:
                if new_password==confirm_password:
                    teacher_obj.password=new_password
                    teacher_obj.save()
                    return HttpResponse('Password Reset Successfully')
                else:
                    msg='New Password and Confrim Password is not matching'
                    return render(request,'password_reset_manually.html',{'msg':msg})
            else:
                msg='Current Password You Entered is Wrong'
                return render(request,'teacher/password_reset_manually.html',{'msg':msg})
            


# --------------------------------------- LOGIN WITH OTP -------------------------------


class LoginEmailOtp(View):
    def get(self, request):
        return render(request, 'teacher/otp.html')
    
    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            print(email)
            teacher = Teacher.objects.get(email=email)
            
            # checking wheather teacher exist in given username and password
            if teacher is not None:
                request.session['teacher'] = teacher.id  # creating a sesseion for teacher to get teacher object in next View(OtpVerification(View))
                otp = get_random_string(length=6, allowed_chars='1234567890')
                expiration_time = datetime.now() + timedelta(minutes=5)
                expiration_time_str = expiration_time.strftime('%Y-%m-%d %H:%M:%S')
                
                subject = 'OTP for Login'
                message = f'Your OTP for login account : {otp}'
                from_email = settings.EMAIL_HOST_USER
                to_email_list = [email]
                send_mail(subject, message, from_email, to_email_list)
                request.session['otp'] = {'code': otp, 'expiration_time_string': expiration_time_str}
                return redirect('otp_verify')
            else:
                msg = 'user does not exist'
                return render(request, 'teacher/otp.html', {'msg': msg})
        else:
            return render(request, 'teacher/otp.html')
        

# --------------------------------------- OTP VERIFICATION -------------------------------


class OtpVerification(View):
    def get(self, request):
        return render(request, 'teacher/otp_verification.html')
    
    def post(self, request):
        if request.method == 'POST':
            otp_entered = request.POST.get('otp')
            otp_session = request.session.get('otp')
            if otp_session:
                saved_otp = otp_session.get('code')
                expiry_time = otp_session.get('expiration_time_string')
                expiration_time = datetime.strptime(expiry_time, '%Y-%m-%d %H:%M:%S')
                if datetime.now() <= expiration_time:
                    if saved_otp and otp_entered == saved_otp:
                        teacher_obj = request.session.get('teacher')
                        teacher = Teacher.objects.get(id=teacher_obj)
                        login(request, teacher)
                        return render(request, 'teacher/teacher_profile.html', {'teacher': teacher})
                    else:
                        msg = 'wrong otp'
                        return render(request, 'teacher/otp_verification.html', {'msg': msg})
                else:
                    msg1 = 'Otp expired'
                    return render(request, 'teacher/otp_verification.html', {'msg1': msg1})
                


# --------------------------------------- UPLOAD Files -------------------------------


class AddCourseMaterial(View):
    def get(self, request):
        form = CourseMaterialForm()
        return render(request, 'uploadfiles/add_course_material.html', {'form': form})

    def post(self, request):
        form = CourseMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacherapp:course_material_list')
        else:
            return HttpResponse('Validation failed')
        

class CourseMaterialList(View):
    def get(self, request):
        materials = CourseMaterial.objects.all()
        print(materials)
        return render(request, 'uploadfiles/course_material_list.html', {'materials': materials})
    

class UpdateCourseMaterial(View):
    def get(self, request, id):
        material = CourseMaterial.objects.get(id=id)
        form = CourseMaterialForm(instance=material)
        return render(request, 'uploadfiles/update_course_material.html', {'form': form})
    

    def post(self, request, id):
        material = CourseMaterial.objects.get(id=id)
        form = CourseMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('teacherapp:course_material_list')
        else:
            return HttpResponse('Validation failed')
        

class DeleteCourseMaterial(View):
    def get(self, request, id):
        material_obj = CourseMaterial.objects.get(id=id)
        material_obj.delete()
        return redirect('teacherapp:course_material_list')


# --------------------------------------- Teacher Attendance  -------------------------------


class MarkAttendanceView(View):
    def get(self, request):
        form = TeacherAttendanceForm()
        return render(request, 'teacherAttendance/mark_attendance.html', {'form': form})

    def post(self, request):
        form = TeacherAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance-success')
        return render(request, 'teacherAttendance/mark_attendance.html', {'form': form})

class AttendanceSuccessView(View):
    def get(self, request):
        attendances=TeacherAttendance.objects.all()
        return render(request, 'teacherAttendance/attendance_success.html',{'attendances':attendances})
    
    
class UpdateAttendanceView(View):
    def get(self, request, pk):
        attendance = TeacherAttendance.objects.get( pk=pk)
        form = TeacherAttendanceForm(instance=attendance)
        return render(request, 'teacherAttendance/update_attendance.html', {'form': form})
    
    def post(self, request, pk):
        attendance = TeacherAttendance.objects.get(pk=pk)
        form = TeacherAttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance-success')
        return render(request, 'teacherAttendance/update_attendance.html', {'form': form})
    
    
class DeleteAttendanceView(View):
    def get(self, request, pk):
        attendance =TeacherAttendance.objects.get(pk=pk)
        attendance.delete()
        return redirect('attendance-success')
    

#-------------------------------View students--------------------------------------------------

class ViewStudents(View):
    def get(self,request,course,batch):
        students=Student.objects.filter(course=course,batch=batch)
        return render(request,'teacher/view_studentsTeacher.html',{'students':students})
    
    


