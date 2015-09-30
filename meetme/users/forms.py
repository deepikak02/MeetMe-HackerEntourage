__author__ = 'hacker'

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class MMUserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

    def save(self, commit=True):
        user = super(MMUserCreationForm, self).save(False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class MMUserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']





