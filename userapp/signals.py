from django.contrib.auth.models import User
from .models import ProfileModel
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def create_profile(sender,created,instance,*args,**kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
