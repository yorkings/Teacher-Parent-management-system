from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CHOICES = [
        ('admin', 'ADMIN'),
        ('parent', 'PARENT'),
        ('teacher', 'TEACHER')
    ]
    role = models.CharField(choices=CHOICES, default='admin', max_length=10)

class events(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(blank=True,null=True,upload_to="events")
    details=models.TextField()
    def __str__(self):
        return self.title

