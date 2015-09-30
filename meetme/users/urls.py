__author__ = 'hacker'

from django.views.generic import TemplateView
from django.conf.urls import include,url
import views

urlpatterns = [
    url(r'^register/$', views.UserCreateView.as_view(template_name='users/register.html'),name='register'),
    url(r'^login/$', views.UserLoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'^logout/$', views.LogoutView.as_view(),name='logout'),
]