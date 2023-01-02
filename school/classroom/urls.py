from django.urls import path
from .views import HomeView, ThankYouView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView,TeacherUpdateView, TeacherDeleteView


app_name = 'classroom'

urlpatterns = [
    
path('', HomeView.as_view(), name='home'),
path('thank_you/', ThankYouView.as_view(), name ='thank_you'),
path('contact/', ContactFormView.as_view(), name='contact'),
path('teacher/', TeacherCreateView.as_view(), name= 'teacher'),
path('teacher_list/', TeacherListView.as_view(), name='teacher_list'),
path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name = 'teacher_detail'),
path('teacher_update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
path('delete_teacher/<int:pk>/', TeacherDeleteView.as_view(), name='delete_teacher')


]
