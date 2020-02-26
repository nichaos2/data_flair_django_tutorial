from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

from .models import Student

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})


# for the redirect
class tutorial(RedirectView): 
    url = 'https://data-flair.training/blogs/category/django'


# cookies
def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django tutorial</h1><br>cookies?")
    if request.COOKIES.get('visits'):
        value=int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value+1)
        html.set_cookie('dataflair', 'Welcome Back')
    else:
        value = 1
        text = 'Welcome for the first time'
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html

def showcookie(request):
    # if we visit this page ('showcookie') before visiting the page 'setcookie'
    #  it will thorw an error in value as None it cannot be printed
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        print(value) # int;  None if we visit this page without visting the setcookie
        text = request.COOKIES.get('dataflair')
        print(text)
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))    
        html.set_cookie('visits', int(value)+1)
        return html
    else:
        return redirect(setcookie) # is this the right way to redirect
