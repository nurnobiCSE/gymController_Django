from django.db import models

# Create your models here.
class userForm(models.Model):
    name = models.CharField(max_length=25,blank=False)
    phone = models.CharField(max_length=25,blank=False)
    email = models.CharField(max_length=25,blank=False)
    nid = models.CharField(max_length=25,blank=False)
    address = models.CharField(max_length=250,blank=False)
    gender = models.CharField(max_length=25,blank=False)
    pass1 = models.CharField(max_length=25,blank=False)
    pass2 = models.CharField(max_length=30,blank=False)
    schedule = models.CharField(max_length=25,blank=False,default=" ")
    def __str__(self):
        return self.name + " ("+str(self.id)+")"

