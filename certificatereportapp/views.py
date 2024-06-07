from django.shortcuts import render,redirect,HttpResponse
from .forms import SubjectForm,ReportcardForm
from django.views import View
from .models import Student,Reportcard,Subject
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas





# Create your views here.

# --------------------------------------- Subjects  -------------------------------

class SubjectListView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(request, 'subject/sub_list.html', {'subjects': subjects})
    
    
class SubjectCreateView(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, 'subject/subject_form.html', {'form': form})
    
    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        return render(request, 'subject/subject_form.html', {'form': form})
    

class SubjectUpdateView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        form = SubjectForm(instance=subject)
        return render(request, 'subject/subject_update.html', {'form': form})
    
    def post(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        

class SubjectDeleteView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return redirect('subject_list')


# --------------------------------------- Report Card  -------------------------------   

class ReportCardListView(View):
    def get(self, request):
        reportcards = Reportcard.objects.all()
        return render(request, 'reportcard/report_list.html', {'reportcards': reportcards})
    
    
class ReportCardCreateView(View):
    def get(self, request):
        form = ReportcardForm()
        return render(request, 'reportcard/report_form.html', {'form': form})
    def post(self, request):
        form = ReportcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reportcard_list')
        return render(request, 'reportcard/report_form.html', {'form': form})
    
class ReportCardUpdateView(View):
    def get(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        form = ReportcardForm(instance=reportcard)
        return render(request, 'reportcard/report_form.html', {'form': form, 'reportcard': reportcard})
    
    def post(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        form = ReportcardForm(request.POST, instance=reportcard)
        if form.is_valid():
            form.save()
            return redirect('reportcard_list')
        return render(request, 'reportcard/report_form.html', {'form': form, 'reportcard': reportcard})
    

class ReportCardDeleteView(View):
    def get(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        reportcard.delete()
        return redirect('reportcard_list')



class ReportCardView(View):
    def get(self, request, pk):
        reportcard = Reportcard.objects.get(pk=pk)
        context = {
            'student_name': reportcard.stuname.first_name,
            'total_marks': reportcard.total_marks(),
            'total_grade':reportcard.total_grade(),
            'performance': reportcard.performance(),
        }
        return render(request, 'reportcard/reportcard.html', context)



# --------------------------------------- Course Completion Certificate  -------------------------------
  

class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'student/studentlist.html', context)
    


class GenerateCertificateView(View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{student.first_name}_{student.last_name}_certificate.pdf"'
        
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter
        p.setFont("Helvetica", 12)
        
        # Draw the certificate content

        # p.drawString(200, height - 50, "Course Completion Certificate")
        # p.drawString(100, height - 100, f"This is to certify that {student.first_name} {student.last_name} ")
        # p.drawString(100, height - 150, f" has successfully completed the {student.course.course_name} course.")
        
        #the above fourline code is enough for certificate generation. below code is to just for more styling

        p.setFont("Helvetica-Bold", 24)
        p.drawCentredString(width / 2.0, height - 100, "Certificate of Completion")
        p.setFont("Helvetica", 18)
        p.drawCentredString(width / 2.0, height - 150, "This is to certify that")
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2.0, height - 200, f"{student.first_name} {student.last_name}")
        p.setFont("Helvetica", 18)
        p.drawCentredString(width / 2.0, height - 250, "has successfully completed the course")
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2.0, height - 300, f"{student.course.course_name}")
        p.setFont("Helvetica", 16)
        p.drawCentredString(width / 2.0, height - 450, "Congratulations!")
        # Add a border (optional)
        p.rect(30, 30, width - 60, height - 60)

        # Save the PDF file
        p.showPage()
        p.save()
        
        return response