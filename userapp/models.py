from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default1.jpg',upload_to='media', validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])
    def __str__(self):
        return self.user.username
