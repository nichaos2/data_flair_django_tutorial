from django.shortcuts import render
from . import forms

def regform(request):
    form = forms.SignUp
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html += " this form is valid"
    else: 
        html = 'Welcome fot the first time'
    return render(request, 'signup.html', {'html':html, 'form':form})
