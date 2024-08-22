"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),  # so we created a homepage here now if we want to show project stuff like project objects (java course , python course)
    path('blog/', include('blog.urls')),    # so in here we include all the urls in blog project to have access to them in here too => localhost:8000/blog/blog # for this we needed to create a urls.py which contains the blog urls and connect them to views in blog folder by importing them and making a templates
]


# we added this to get MEDIA_ROOT and MEDIA_URL
from django.conf.urls.static import static      # we added this here
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # we added this: so when we want to get the file from user
                # and save it in our MEDIA_URL and MEDIA_ROOT we need to add this line too
