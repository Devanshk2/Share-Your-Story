from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True,blank=True)
    title=models.CharField(max_length=50,blank=True)
    author=models.CharField(max_length=50,blank=True)
    content=models.TextField(blank=True)
    slug=models.CharField(max_length=100,blank=True )
    # timestamp=models.DateTimeField(blank=True,null=False)
    timestamp=models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    # last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    
    def __str__(self):
        return self.title +' by '+self.author
    
    def get_absolute_url(self):
        return reverse('blogpost', kwargs={'slug': self.slug}) 