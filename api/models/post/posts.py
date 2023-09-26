from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=256)
    content = models.TextField(max_length=5000,null=True,blank=True)

    def __str__(self):
        return self.title