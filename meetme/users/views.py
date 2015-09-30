from django.shortcuts import render
from django.views.generic import CreateView, FormView, View
from django.contrib.auth.models import User
from forms import MMUserCreationForm, MMUserLoginForm
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = MMUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        print "In get success url"
        if self.object:
            form = self.get_form()
            if form.is_valid():
                print "Form is valid"
                user = authenticate(username = self.object.username,password = form.cleaned_data['password'])
                print "User is",user
                login(self.request,user)
        return self.success_url

class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = MMUserLoginForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        if form.is_valid():
            print "Form is valid"
            u = User.objects.get(email = form.cleaned_data['email'])
            user = authenticate(username = u.username,password = form.cleaned_data['password'])
            print "User is",user
            login(self.request,user)
        return super(UserLoginView, self).form_valid(form)

class LogoutView(View):
    def get(self,request):
        print request.user
        if request.user.is_authenticated():
            logout(request)
        return HttpResponseRedirect(reverse('users:register'))

        


