from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    issue=models.TextField()
    phone=models.CharField(max_length=15)
    # time=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return 'message from '+self.name+' - '+self.email
    