from django.db import models

# Create your models here.

# for working with data base:

class Project(models.Model):

    # when ever you want to add a property or a field, use the models module

    title = models.CharField(max_length=100)        # using model field django to create a string
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')    # for this you need to install pillow module
    url = models.URLField(blank=True)

    # after creating our fields or attributes we need to add these to data base by using: python manage.py migrate and python manage.py makemigrations
    
    
    # so if you look at admin page and go to projects you cant see the projects name, this will shows the projects name 
    # you dont need to migrate or makemigrate here because the function has nothing to do with the data base. there are attributes and fields that changes and have to migrate them
    # DO THIS FOR BLOG PROJECTS TOO!
    # be careful to create this method in class not outside!!!!!
    def __str__(self):
        return self.title