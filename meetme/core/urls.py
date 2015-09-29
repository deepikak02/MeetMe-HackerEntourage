__author__ = 'hacker'

from django.views.generic import TemplateView
from django.conf.urls import include,url

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'),name='home'),
]