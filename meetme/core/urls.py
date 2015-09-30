__author__ = 'hacker'

from django.views.generic import TemplateView
from django.conf.urls import include,url
import views

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='core/home.html'),name='home'),
    url(r'^$', views.IndexView.as_view(),name='index'),
    ]
