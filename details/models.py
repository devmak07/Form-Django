from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
class form_detail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField(max_length=300)
    age=models.IntegerField()
    date=models.DateField(null=True,blank=True)
    boolean=models.BooleanField()
    file=models.FileField(null=True,blank=True)
    department=models.ForeignKey(Department,null=True,blank=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.name
