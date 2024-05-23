from django.db import models
from django.urls import reverse

# Create your models here.

class Email(models.Model):
    
     name = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     to_email = models.CharField(max_length=255)
     message = models.CharField(max_length=255)

     def __str__(self):
        return self.name

     def get_absolute_url(self):
             return reverse('home')