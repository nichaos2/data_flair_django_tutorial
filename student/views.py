from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})
