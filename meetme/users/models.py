from django.db import models
from django.contrib.auth.models import User
from ..core.models import BaseMMModel
from  django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class MMUser(BaseMMModel):
    user = models.OneToOneField(User, primary_key=True)

@receiver(post_save,sender = User)
def check_for_MMUser(sender,**kwargs):
    if MMUser.objects.filter(user = kwargs['instance']).count() > 0:
        return
    else:
        MMUser.objects.create(user=kwargs['instance'])


