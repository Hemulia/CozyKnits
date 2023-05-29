from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=150)
    instructions = models.TextField(null = True, blank = True)
    start_time = models.DateTimeField(auto_now_add = True)
    end_time = models.DateTimeField( null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Yarn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255,blank=True)
    brand = models.CharField(max_length=155, blank=True)
    weight = models.CharField(max_length=20, blank=True) 
    length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null = True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null= True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.brand}"
