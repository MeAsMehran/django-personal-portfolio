
# WE CREATED THIS FILE FOR URLS #


app_name = 'blog'       # for blog.html file(read there)

from django.urls import path
from . import views     # the . means current directory

urlpatterns = [
    # path('', views.home, name="home"),  # so we created a homepage here now if we want to show project stuff like project objects (java course , python course)
    path('blog/', views.blog_allUrls, name='blogUrls'),      #localhost:8000/blog/blog
    path('<int:blog_id>', views.detail, name='detail'),

]
