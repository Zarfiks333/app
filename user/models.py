from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True, verbose_name='аватарка пользователя')
    username = models.CharField(max_length=150, unique=True ,verbose_name='имя пользователя')
     
    
    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.username