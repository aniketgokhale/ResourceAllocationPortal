from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [

    # /student/login_page
    url(r'^login_page/$', views.StudentLoginView.as_view(), name='login'),

    # /student/dashboard
    url(r'^dashboard/$', views.dashboard_view, name='dashboard'),

]
