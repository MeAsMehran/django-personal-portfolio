from django.db import models

# Create your models here.

class BlogModel(models.Model):

    linkTitle = models.CharField(max_length=100)
    shortInfo = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)       # if we dont want to make url for the new project created in admin section we add blank=True
