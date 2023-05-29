from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=150)
    instructions = models.TextField(null = True, blank = True)
    start_time = models.DateTimeField(auto_now_add = True)
    end_time = models.DateTimeField(auto_now = True, null = True)

    def __str__(self):
        return self.name
    
class Yarn(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=155)
    weight = models.CharField(max_length=20) 
    length = models.DecimalField(max_digits=5, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return f"{self.name}, {self.brand}"
