from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import RedirectView

from .models import Student

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})


class tutorial(RedirectView): 
    url = 'https://data-flair.training/blogs/category/django'