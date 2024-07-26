from django.urls import path
from .views import SubjectListView,SubjectCreateView,SubjectUpdateView,SubjectDeleteView,ReportCardCreateView,ReportCardUpdateView,ReportCardDeleteView,ReportCardView,StudentListView, GenerateCertificateView,ReportCardListView,ImportDataView,ExportToExcelView


urlpatterns = [

    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjectscreate', SubjectCreateView.as_view(), name='subject_create'),
    path('subjectsupdate/<int:pk>/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subjectsdelete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
    
    path('reportlist/',ReportCardListView.as_view(),name='reportcard_list'),
    path('reportcreate/', ReportCardCreateView.as_view(), name='reportcard_create'),
    path('reportupdate/<int:pk>/', ReportCardUpdateView.as_view(), name='reportcard_update'),
    path('reportdelete/<int:pk>/', ReportCardDeleteView.as_view(), name='reportcard_delete'),
    path('achievement/<int:pk>/', ReportCardView.as_view(), name='achievement_view'),

    path('students/', StudentListView.as_view(), name='student_list'),
    path('generate_certificate/<int:student_id>/', GenerateCertificateView.as_view(), name='generate_certificate'),
    
    path('import/', ImportDataView.as_view(), name='import_data'),
    path('export/', ExportToExcelView.as_view(), name='export_data'),

]