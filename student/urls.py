from django.urls import path
from .views import *

# the url has to provide the student/
# localhost:port/student --> student_show
# localhost:port/student/djangotutor --> tutorial.as_view()
urlpatterns = [
    path('', student_show, name='student_show'),
    path('djangotutor/', tutorial.as_view(), name='redirect'),
    path('set_cookie/', setcookie),
    path('show_cookie/', showcookie),
    path('delete_cookie/', deletecookie),
    path('test_cookie/', cookie_session),
    path('test_cookie_delete/', cookie_delete),
    path('create_session/', create_session),
    path('access_session/', access_session),
    path('delete_session/', delete_session),
]
