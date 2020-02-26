from django.urls import path
from .views import *

# the url has to provide the student/
# localhost:port/student --> student_show
# localhost:port/student/djangotutor --> tutorial.as_view()
urlpatterns = [
    path('', student_show, name = 'student_show'),
    path('djangotutor/', tutorial.as_view(), name = 'redirect')
]