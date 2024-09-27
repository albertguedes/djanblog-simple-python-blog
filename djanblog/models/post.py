from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256,null=False,default='')
    description = models.CharField(max_length=512,null=False,default='')
    content = models.TextField(null=False,default='')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
