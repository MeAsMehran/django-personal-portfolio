from django.contrib import admin
from .models import Project         # we added

# Register your models here.

admin.site.register(Project)    # this line will show us the project model in our admin page

