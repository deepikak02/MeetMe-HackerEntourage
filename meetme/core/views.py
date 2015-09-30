from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.


class IndexView(View):
    def get(self,request):
        print request.user
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('core:home'))
        return HttpResponseRedirect(reverse('users:register'))