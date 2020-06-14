from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    repository = models.CharField(max_length=100)
    technologies_used = models.CharField(max_length=50)
    live_link = models.URLField(max_length = 200)
    photo_web = models.ImageField(upload_to='webs/', null=True)
    
    def __str__(self):
        return self.name

    def save_project(self):
        self.save()    

      