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


    def clean(self):
        super(MMUserCreationForm, self).clean()
        if User.objects.filter(username = self.cleaned_data['username']).count() > 0:
            raise ValidationError('User with that username already exists. Please pick a different username')
        if User.objects.filter(email = self.cleaned_data['email']).count() > 0:
            raise ValidationError('User with that email already exists. Please pick a different email')
        return self.cleaned_data

