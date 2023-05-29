from django.contrib import admin
from . import models

myModels = [models.Project, models.Yarn]
admin.site.register(myModels)
